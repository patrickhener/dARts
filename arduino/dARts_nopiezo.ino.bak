/* Pins definieren */
// Ultraschall
const int trigPin = 9;
const int echoPin = 10;
// Button
const int buttonPin = 2;
const int buttonLedPin = 4;

// Matrix
const int PO_01 = 46;
const int PO_02 = 48;
const int PO_03 = 25;
const int PO_04 = 23;

const int PI_01 = 50; // = 49;
const int PI_02 = 52; // = 47;
const int PI_03 = 53; // = 45;
const int PI_04 = 51; // = 43;
const int PI_05 = 49; // = 41;
const int PI_06 = 47; // = 39;
const int PI_07 = 45; // = 37;
const int PI_08 = 43; // = 35;
const int PI_09 = 41; // = 33;
const int PI_10 = 39; // = 31;
const int PI_11 = 37; // = 29;
const int PI_12 = 35; // = 27;
const int PI_13 = 33; // = 25;
const int PI_14 = 31; // = 23;
const int PI_15 = 29; // = 28;
const int PI_16 = 27; // = 26;

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

/* Variablen */
// Piezo
int wert = 0;
int schwelle = 300;
// Button
int buttonState = 0;
// Ultraschall
long duration;
int distance;
int ultraschwelle = 10;

/* Setup loop */
void setup() {
	// Pins für Ultraschall
	pinMode(trigPin, OUTPUT);
	pinMode(echoPin, INPUT);
	// Pin für Button
	pinMode(buttonPin, INPUT_PULLUP);
	// Pin für Button LED
	pinMode(buttonLedPin, OUTPUT);
	digitalWrite(buttonLedPin, HIGH);
	// Matrix
	pinMode(PO_01, OUTPUT);
  	pinMode(PO_02, OUTPUT);
	pinMode(PO_03, OUTPUT);
	pinMode(PO_04, OUTPUT);

	pinMode(PI_01, INPUT_PULLUP);
	pinMode(PI_02, INPUT_PULLUP);
	pinMode(PI_03, INPUT_PULLUP);
	pinMode(PI_04, INPUT_PULLUP);
	pinMode(PI_05, INPUT_PULLUP);
	pinMode(PI_06, INPUT_PULLUP);
	pinMode(PI_07, INPUT_PULLUP);
	pinMode(PI_08, INPUT_PULLUP);
	pinMode(PI_09, INPUT_PULLUP);
	pinMode(PI_10, INPUT_PULLUP);
	pinMode(PI_11, INPUT_PULLUP);
	pinMode(PI_12, INPUT_PULLUP);
	pinMode(PI_13, INPUT_PULLUP);
	pinMode(PI_14, INPUT_PULLUP);
	pinMode(PI_15, INPUT_PULLUP);
	pinMode(PI_16, INPUT_PULLUP);
	// Beginne serielle Übertragung an PC
	Serial.begin(9600);
}

/* Main loop */
void loop() {
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


	/* Button */
	// Button einlesen
	buttonState = digitalRead(buttonPin);
	// Wenn Button gedrückt, dann Schreibe DANEBEN und lass den Button blinken
	// In dieser Zeit sollte das Python Script die Misses mit nullen auffüllen
	// Dann muss der Button nochmals gedrückt werden, damit der nächste Spieler dran ist
	if (buttonState == LOW) {
		Serial.println("KNOPF");
		digitalWrite(buttonLedPin, LOW);
		delay(500);
		digitalWrite(buttonLedPin, HIGH);
		delay(500);
		digitalWrite(buttonLedPin, LOW);
		delay(500);
		digitalWrite(buttonLedPin, HIGH);
		delay(500);
		digitalWrite(buttonLedPin, LOW);
		delay(500);
		digitalWrite(buttonLedPin, HIGH);
		delay(500);
	}

	/* Matrix */

	// Reihe 0 auslesen in Bool Array
	digitalWrite(PO_01, LOW);
	digitalWrite(PO_02, HIGH);
	digitalWrite(PO_03, HIGH);
	digitalWrite(PO_04, HIGH);
	bI[0][0]  = digitalRead(PI_01);
	bI[0][1]  = digitalRead(PI_02);
	bI[0][2]  = digitalRead(PI_03);
	bI[0][3]  = digitalRead(PI_04);
	bI[0][4]  = digitalRead(PI_05);
	bI[0][5]  = digitalRead(PI_06);
	bI[0][6]  = digitalRead(PI_07);
	bI[0][7]  = digitalRead(PI_08);
	bI[0][8]  = digitalRead(PI_09);
	bI[0][9]  = digitalRead(PI_10);
	bI[0][10] = digitalRead(PI_11);
	bI[0][11] = digitalRead(PI_12);
	bI[0][12] = digitalRead(PI_13);
	bI[0][13] = digitalRead(PI_14);
	bI[0][14] = digitalRead(PI_15);
	bI[0][15] = digitalRead(PI_16);

	// Reihe 1 auslesen in Bool Array
	digitalWrite(PO_01, HIGH);
	digitalWrite(PO_02, LOW);
	digitalWrite(PO_03, HIGH);
	digitalWrite(PO_04, HIGH);
	bI[1][0]  = digitalRead(PI_01);
	bI[1][1]  = digitalRead(PI_02);
	bI[1][2]  = digitalRead(PI_03);
	bI[1][3]  = digitalRead(PI_04);
	bI[1][4]  = digitalRead(PI_05);
	bI[1][5]  = digitalRead(PI_06);
	bI[1][6]  = digitalRead(PI_07);
	bI[1][7]  = digitalRead(PI_08);
	bI[1][8]  = digitalRead(PI_09);
	bI[1][9]  = digitalRead(PI_10);
	bI[1][10] = digitalRead(PI_11);
	bI[1][11] = digitalRead(PI_12);
	bI[1][12] = digitalRead(PI_13);
	bI[1][13] = digitalRead(PI_14);
	bI[1][14] = digitalRead(PI_15);
	bI[1][15] = digitalRead(PI_16);

	// Reihe 2 auslesen in Bool Array
	digitalWrite(PO_01, HIGH);
	digitalWrite(PO_02, HIGH);
	digitalWrite(PO_03, LOW);
	digitalWrite(PO_04, HIGH);
	bI[2][0]  = digitalRead(PI_01);
	bI[2][1]  = digitalRead(PI_02);
	bI[2][2]  = digitalRead(PI_03);
	bI[2][3]  = digitalRead(PI_04);
	bI[2][4]  = digitalRead(PI_05);
	bI[2][5]  = digitalRead(PI_06);
	bI[2][6]  = digitalRead(PI_07);
	bI[2][7]  = digitalRead(PI_08);
	bI[2][8]  = digitalRead(PI_09);
	bI[2][9]  = digitalRead(PI_10);
	bI[2][10] = digitalRead(PI_11);
	bI[2][11] = digitalRead(PI_12);
	bI[2][12] = digitalRead(PI_13);
	bI[2][13] = digitalRead(PI_14);
	bI[2][14] = digitalRead(PI_15);
	bI[2][15] = digitalRead(PI_16);

	// Reihe 3 auslesen in Bool Array
	digitalWrite(PO_01, HIGH);
	digitalWrite(PO_02, HIGH);
	digitalWrite(PO_03, HIGH);
	digitalWrite(PO_04, LOW);
	bI[3][0]  = digitalRead(PI_01);
	bI[3][1]  = digitalRead(PI_02);
	bI[3][2]  = digitalRead(PI_03);
	bI[3][3]  = digitalRead(PI_04);
	bI[3][4]  = digitalRead(PI_05);
	bI[3][5]  = digitalRead(PI_06);
	bI[3][6]  = digitalRead(PI_07);
	bI[3][7]  = digitalRead(PI_08);
	bI[3][8]  = digitalRead(PI_09);
	bI[3][9]  = digitalRead(PI_10);
	bI[3][10] = digitalRead(PI_11);
	bI[3][11] = digitalRead(PI_12);
	bI[3][12] = digitalRead(PI_13);
	bI[3][13] = digitalRead(PI_14);
	bI[3][14] = digitalRead(PI_15);
	bI[3][15] = digitalRead(PI_16);

	bHitDetected = false;

	// Prüfen ob im Array etwas getroffen wurde
	// Wenn ja Wert ausgeben
	for (int x=3; x>=0; x--)
	{
		for (int y=0; y<16; y++)
		{
			if (bI[x][y] == 0)
			{
				Serial.println(FAKTOR_WERTE[x][y]);
				delay(iHitPause);
				bHitDetected = true;
				// Zur Sicherheit - Bulls auf NULL
				bI[1][10] = 1;
				bI[2][10] = 1;
			}
		}
	}
}
