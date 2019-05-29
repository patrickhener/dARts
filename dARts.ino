/* Pins definieren */
// Ultraschall
const int trigPin = 9;
const int echoPin = 10;
// Piezo
const int piezoPin = A0;
// Button
const int buttonPin = 2;
// Debug LED für Button Test
const int ledPin = 4;

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
	// DEBUG Pin für LED
	pinMode(ledPin, OUTPUT);
	digitalWrite(ledPin, LOW);
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
		Serial.println("Spieler holt Pfeile");
	}

	/* Piezo */
	// Eingangswert an A0 lesen
	wert = analogRead(piezoPin);
	// Wenn Wert größer Schwellwert - dann Aktion
	if (wert >= schwelle) {
		// Bislang nur Ausgabe
		Serial.println("Piezo ausgelöst");
		// Der Piezo braucht einige Zeit, um sich wieder zu beruhigen, daher 200ms warten.
		delay(200);
	}

	/* Button */
	// Button einlesen
	buttonState = digitalRead(buttonPin);
	// Wenn Button gedrückt, dann LED schalten, bislang
	if (buttonState == LOW) {
		Serial.println("Knopf wurde gedrückt");
		digitalWrite(ledPin, HIGH);
		delay(1000);
	} else {
		digitalWrite(ledPin, LOW);
	}
}
