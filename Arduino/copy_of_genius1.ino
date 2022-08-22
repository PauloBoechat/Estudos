#define RED 1
#define GREEN 2
#define BLUE 3


int pin_red = 7;
int pin_green = 6;
int pin_blue = 4;


int pins[4] = {7, 6, 4}; // RED, GREEN, BLUE, YELLOW

int btn_red = 9;
int btn_green = 12;
int btn_blue = 11;


int blinkTime = 50;

int timeOn = 1000;
int timeOff = 500;
int timeTurnOff = 350;
int timeTurnOn = 200;
int waitNextRound = 2000;

int sequencia[20];
int actual = 1;

bool acertou = true;

void setup()
{
  Serial.begin(9600);
  
  configurarJogo();
  
  pinMode(btn_red, INPUT_PULLUP);
  pinMode(btn_green, INPUT_PULLUP);
  pinMode(btn_blue, INPUT_PULLUP);
}

void loop()
{
  for(int i = 0; i < actual; i++)
    ligarLed(sequencia[i]);
  
  piscarLeds();
  
  // Ler botões e verificar se acertou
  for(int i = 0; i < actual;) {
    if(digitalRead(btn_red) == LOW) {
      blink(pin_red);
      if(sequencia[i] == RED)
      	i++;
      else {
        acertou = false;
        break;
      }
    }
    else if(digitalRead(btn_green) == LOW) {
      blink(pin_green);
      if(sequencia[i] == GREEN)
      	i++;
      else {
        acertou = false;
        break;
      }
    }
    else if(digitalRead(btn_blue) == LOW) {
      blink(pin_blue);
      if(sequencia[i] == BLUE)
      	i++;
      else {
        acertou = false;
        break;
      }
    }
  }
  
  if(acertou) {
  	actual++;
    sinalizarAcerto();
  }
  else
    configurarJogo();
  
  delay(waitNextRound);
}

void sinalizarAcerto() {
  int time = 300;
  delay(800);
  for(int i = 0; i < 1; i++) {
    digitalWrite(pin_red, HIGH);
    delay(time);
    digitalWrite(pin_red, LOW);
    digitalWrite(pin_green, HIGH);
    delay(time);
    digitalWrite(pin_green, LOW);
    digitalWrite(pin_blue, HIGH);
    delay(time);
    digitalWrite(pin_blue, LOW);
  }
}

void configurarJogo() {
  actual = 1;
  acertou = true;
  
  randomSeed(analogRead(0));
  
  for(int i = 0; i < 20; i++) {
    sequencia[i] = random(1, 4);
  }
  
  digitalWrite(pin_red, HIGH);
  digitalWrite(pin_green, HIGH);
  digitalWrite(pin_blue, HIGH);
  delay(3000);
  digitalWrite(pin_red, LOW);
  digitalWrite(pin_green, LOW);
  digitalWrite(pin_blue, LOW);
  delay(1000);
}

void piscarLeds() {
  for(int i = 0; i < 3; i++) {
    digitalWrite(pin_red, HIGH);
    digitalWrite(pin_green, HIGH);
    digitalWrite(pin_blue, HIGH);
    delay(timeTurnOn);
    digitalWrite(pin_red, LOW);
    digitalWrite(pin_green, LOW);
    digitalWrite(pin_blue, LOW);
    delay(timeTurnOff);
  }
}

void ligarLed(int numLed) {
  digitalWrite(pins[numLed-1], HIGH);
  delay(timeOn);
  digitalWrite(pins[numLed-1], LOW);
  delay(timeOff);
}

void blink(int pin) {
  digitalWrite(pin, HIGH);
  delay(blinkTime);
  digitalWrite(pin, LOW);
}