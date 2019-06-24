/***********************/
/*        PINS         */
/***********************/
// Ultraschall
const int echoPin = 8;
const int trigPin = 9;
// Piezo
const int piezoPin[2] = { A0, A1 };
// Button
const int buttonPin = 2;
const int buttonLedPin = 3;

// Matrix
// Output Pins
const int PO_[4] = { 22, 24, 49, 47 };
// Input Pins
const int PI_[16] = { 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 53, 51 };

/***********************/
/*        VARIABLEN    */
/***********************/
// Matrix Werte
// 120 = single 20, 220 = double 20, 320 = triple 20
// 125 = single Bull, 225 = doppel bull
// 4x16 = 64, aber nur 62 Zahlenwerte, deshalb kommt zweimal 000 vor
// usw..
const int FAKTOR_WERTE[4][16]={
	{212, 112, 209, 109, 214, 114, 211, 111, 208, 108, 000, 312, 309, 314, 311, 308},
	{216, 116, 207, 107, 219, 119, 203, 103, 217, 117, 225, 316, 307, 319, 303, 317},
	{202, 102, 215, 115, 210, 110, 206, 106, 213, 113, 125, 302, 315, 310, 306, 313},
	{204, 104, 218, 118, 201, 101, 220, 120, 205, 105, 000, 304, 318, 301, 320, 305}
};

bool bI[4][16];
bool bHitDetected = false;
const int iHitPause = 300;
unsigned int iLastThrow = 0;

// Piezo
int wert[2] = { 0, 0 };
int schwelle = 20;
bool bFehlwurf = false;
// Button
int buttonState = 0;
// Ultraschall
long duration;
int distance;
int ultraschwelle = 65;
bool bUsAn = false;
bool bBewegungErkannt = false;
// Input String von PI zu Arduino
String inputString = "";
boolean stringComplete = false;
//
int wurfanzahl = 0;

/***********************/
/*       FUNKTIONEN    */
/***********************/
void Ultraschall() {
	/* Ultraschall */
	// trigPin frei machen
	digitalWrite(trigPin, LOW);
	delayMicroseconds(2);
	// trigPin an für 10 micro secs
	digitalWrite(trigPin, HIGH);
	delayMicroseconds(10);
	digitalWrite(trigPin, LOW);
	// Lesen des Echo Pins
	duration = pulseIn(echoPin, HIGH);
	// Berechnung der Entfernung
	distance = duration*0.034/2;
	// Prüfen ob sich jemand genähert hat
	if (distance <= ultraschwelle) {
		// Bislang ausgabe Seriell
		Serial.println("PFEILE");
	}
}

void checkButton() {
	/* Button */
	// Button einlesen
	buttonState = digitalRead(buttonPin);
	// Wenn gedrückt Ausgabe
	if (buttonState == LOW) {
		Serial.println("KNOPF");
		delay(500);
	}
}


void WurfSchicken(int x, int y) {
	Serial.println(FAKTOR_WERTE[x][y]);
	delay(iHitPause);
	bHitDetected = true;
	// Zur Sicherheit - Bulls auf NULL
	bI[1][10] = 1;
	bI[2][10] = 1;
}

void WurfAuswerten() {
	/* Matrix */
	bHitDetected = false;

	// Reihe 0-3 auslesen in Bool Array
	for (int x=0; x<4; x++) {
		digitalWrite(PO_[0], HIGH);
		digitalWrite(PO_[1], HIGH);
		digitalWrite(PO_[2], HIGH);
		digitalWrite(PO_[3], HIGH);
		digitalWrite(PO_[x], LOW);

		for (int y=0; y<16; y++) {
			bI[x][y]  = digitalRead(PI_[y]);
			// Wenn getroffen dann
			if (bI[x][y] == 0) {
				WurfSchicken(x, y);
			}
		}
	}
}

void FehlwurfErkennen() {
	/* Piezo */
	// Fehlwurf auf false setzen
	bFehlwurf = false;

	// Piezos in Schleife auslesen
	for (int i = 0; i < 2; i++) {
		// Zweifach auslesen um Störungen zu minimieren
		wert[i] = analogRead(piezoPin[i]);
		wert[i] = analogRead(piezoPin[i]);

		if (wert[i] >= schwelle) {
			bFehlwurf = true;
		}
	}

	// Wenn kein Wurf erkannt wurde ist es ein Fehlwurf
	if (!bHitDetected) {
		if (bFehlwurf) {
			// Bislang nur Ausgabe
			Serial.println("FEHLWURF");
			delay(200);
		}
	}
}

void Blinken(int Anzahl) {
	for (int i=0; i<Anzahl; i++) {
		digitalWrite(buttonLedPin, HIGH);
		delay(250);
		digitalWrite(buttonLedPin, LOW);
		delay(250);
	}
}

void ReagiereAufSerialString() {
	if ( inputString.indexOf("BAN") != -1) {
		digitalWrite(buttonLedPin, HIGH);
		bUsAn = true;
	} else if (inputString.indexOf("BAUS") != -1) {
		digitalWrite(buttonLedPin, LOW);
		bUsAn = false;
		bBewegungErkannt = false;
	} else if (inputString.indexOf("PERK") != -1) {
		bBewegungErkannt = true;
	}
	inputString = "";
	stringComplete = false;
}

/***********************/
/* Die einzelnen Loops */
/***********************/

/* Setup loop */
void setup() {
	// Pins für Ultraschall
	pinMode(trigPin, OUTPUT);
	pinMode(echoPin, INPUT);
	// Pin für Button
	pinMode(buttonPin, INPUT_PULLUP);
	// Pin für Button LED
	pinMode(buttonLedPin, OUTPUT);
	digitalWrite(buttonLedPin, LOW);
	// Matrix
	for (int i=0; i<4; i++) {
		pinMode(PO_[i], OUTPUT);
	}

	for (int i=0; i<16; i++) {
		pinMode(PI_[i], INPUT_PULLUP);
	}

	// Button blinken lassen
	Blinken(3);
	// Beginne serielle Übertragung an PC
	Serial.begin(9600);
}

/* Main loop */
void loop() {
	if (!bUsAn) {
		WurfAuswerten();
		FehlwurfErkennen();
		checkButton();
	} else if (bUsAn) {
		checkButton();
		if (!bBewegungErkannt) {
			Ultraschall();
		} else {
			Blinken(1);
		}
	} else {
		Serial.println("Error in Main Loop");
	}

	if(stringComplete)
		ReagiereAufSerialString();
}

/* Für die Kommunikation von PI zu Arduino */
void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    inputString += inChar;
    if (inChar == '\n') {
      stringComplete = true;
    }
  }
}
