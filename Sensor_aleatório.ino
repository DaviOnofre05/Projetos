
// Este projeto é tem um Sensor de Distância Ultrassônico que quando chega perto de uma certa distância ele da um número
// aleatório e este certo número acende um led.

int LED_RED = 8;
int LED_YEL = 9;
int LED_BLU = 10;
int trig = 7;
int echo = 6;

float distancia;

long randNumber;

void setup()
{
  pinMode(LED_RED, OUTPUT);
  pinMode(LED_YEL, OUTPUT);
  pinMode(LED_BLU, OUTPUT);

  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);

  Serial.begin(9600);

  randomSeed(analogRead(0));
  Serial.begin(9600);
  delay(500);
}
void loop()
{

  // sensor

  digitalWrite(trig, LOW);
  delayMicroseconds(5000);
  digitalWrite(trig, HIGH);
  delayMicroseconds(50);
  digitalWrite(trig, LOW);

  distancia = pulseIn(echo, HIGH);
  distancia = distancia / 58;

  Serial.println(distancia);

  // codigo

  if (distancia < 40)
  {
    randNumber = random(1, 4);
    Serial.println(randNumber);

    if (randNumber == 1)
    {
      digitalWrite(LED_BLU, HIGH);
      delay(5000);
      digitalWrite(LED_BLU, LOW);
      delay(100);
    }

    if (randNumber == 2)
    {
      digitalWrite(LED_YEL, HIGH);
      delay(5000);
      digitalWrite(LED_YEL, LOW);
      delay(100);
    }

    if (randNumber == 3)
    {
      digitalWrite(LED_RED, HIGH);
      delay(5000);
      digitalWrite(LED_RED, LOW);
      delay(100);
    }
  }
}