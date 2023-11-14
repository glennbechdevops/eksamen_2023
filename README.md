# Eksamen PGR301 2023

## Krav til leveransen

* Eksamensoppgaven, kode og nødvendig filer er tilgjengelig i GitHub-repo: https://github.com/glennbechdevops/eksamen_2023.
* Når du leverer inn oppgaven via WiseFlow, vennligst opprett et tekstdokument som kun inneholder en kobling til ditt
  repository.
* Vennligst bruk et tekstdokumentformat, ikke PDF, Word eller PowerPoint.
* Du skal ikke opprette en fork av dette repositoryet, men heller kopiere innholdet til et nytt repository.
* Hvis du er bekymret for plagiat fra medstudenter, kan du arbeide i et privat repository og deretter gjøre det
  offentlig tilgjengelig like før innleveringsfristen.

Når sensoren evaluerer oppgaven, vil han/hun:

* Sjekke ditt repository og gå til fanen "Actions" på GitHub for å bekrefte at Workflows faktisk fungerer som de skal.
* Vurdere drøftelsesoppgavene. Du må opprette en "Readme" for besvarelsen i ditt repository. Denne "Readme"-filen skal
  inneholde en grundig beskrivelse og drøfting av oppgavene.
* Sensoren vil opprette en "fork" (en kopi) av ditt repository og deretter kjøre GitHub Actions Workflows med sin egen
  AWS- og GitHub-bruker for å bekrefte at alt fungerer som forventet.

## Om GitHub Free Tier

- I oppgaven blir du bedt om å opprette GitHub Actions Workflows.
- Med GitHub Free Tier har du 2000 minutter med gratis byggetid per måned i private repository.
- Hvis du trenger mer byggetid, har du alternativet å gjøre repositoryet offentlig. Dette vil gi
  deg ubegrenset byggetid. GitHub gir ubegrenset byggetid for offentlige repoer.
- Hvis du er bekymret for at andre kan kopiere arbeidet ditt når repositoryet er offentlig, kan du opprette en ny
  GitHub-bruker med et tilfeldig navn for anonymitet.

## Spesielle hensyn knyttet til Cloud 9

- Løsning på problem med diskplassmangel - informasjon blir delt på Canvas-plattformen.
- Informasjon om rettigheter og sikkerhet i Cloud 9 vil også bli delt på Canvas.

# Evaluering

- Oppgave 1. Kjells Pythonkode - 20 Poeng
- Oppgave 2. Overgang til Java og Spring Boot - 15 Poeng
- Oppgave 3. Terraform, AWS Apprunner og IAC - 15 Poeng
- Oppgave 4. Feedback -30 Poeng
- Oppgave 5. Drøfteoppgaver - 20 poeng

# Oppgavebeskrivelse

I et pulserende teknologisamfunn på Grünerløkka, Oslo, har en livlig oppstart ved navn 'VerneVokterne' funnet
sitt eget nisjeområde innenfor helsesektoren. De utvikler banebrytende programvare for bildebehandling som er
designet
for å sikre at helsepersonell alltid bruker personlig verneutstyr (PPE). Med en lidenskap for innovasjon og et sterkt
ønske om å forbedre arbeidssikkerheten, har 'VerneVokterne' samlet et team av dyktige utviklere, engasjerte designere og
visjonære produktledere.

Selskapet hadde tidligere en veldig sentral utvikler som heter Kjell. Kjell hadde en unik tilnærming til kode,
Dessverre var kvaliteten på Kjells kode, for å si det pent, "kreativ."

Som nyansatt har du blitt gitt den utfordrende oppgaven å overta etter "Kjell," som ikke lenger er en del av selskapet.

![Logo](img/logo.png "Assignment logo")

# Litt om AWS Rekognition

I denne oppgaven skal dere bli kjent med en ny AWS tjeneste.

AWS Rekognition er en tjeneste fra Amazon Web Services som tilbyr avansert bilde- og videoanalyse ved hjelp av
maskinlæringsteknologi. Den har en rekke funksjoner for å gjenkjenne og analysere ulike elementer i bilder og videoer,
inkludert ansiktsgjenkjenning, objektgjenkjenning, tekstgjenkjenning og mer.

AWS Rekognition kan brukes til å identifisere om personer på bilder eller i videoer bruker riktig personlig
beskyttelsesutstyr som hjelmer, vernebriller,
hansker og verneklær. Dette kan være spesielt nyttig i situasjoner der det er viktig å sikre at arbeidere eller
besøkende følger sikkerhetskravene, for eksempel i byggebransjen, industrielle anlegg eller helsevesenet.

Tjenesten kan også tilpasse seg ulike bransjer og bruksområder ved å tillate brukerne å lage
egendefinerte modeller basert på sine egne datasett og krav.

For å bruke AWS Rekognition for PPE-deteksjon, laster du enkelt opp bilder eller videoer til tjenesten, og den vil
deretter analysere innholdet og gi deg informasjon om hvorvidt PPE er tilstede og eventuelt gi posisjonsdata for hvor
PPE er funnet.

Bruk gjerne litt tid til å bli kjent med tjenesten i AWS
miljøet https://eu-west-1.console.aws.amazon.com/rekognition/home

# Oppgave 1. Kjell's Python kode

## A. SAM & GitHub actions workflow

Koden er skrevet som en AWS SAM applikasjon, og ligger i mappen "kjell" i dette repoet. Det er åpenbart at Kjell har
tatt utgangspunkt i et "Hello World" SAM prosjekt og bare brukt navnet sitt som applikasjonsnavn.

* Denne SAM-applikasjonen oppretter en S3 Bucket og du bør sørge for at den lages med ditt kandidatnavn, og du kan under eksamen bruke
  denne bucketen til å laste opp egne bilder for å teste din egen applikasjon.
* I ditt Cloud9-miljø, eller på din egen maskin, kan du bygge og deploye koden til AWS ved å bruke ```sam cli```
* Det anbefales å teste dette før du fortsetter.

Advarsel! Se opp for hardkoding ! Du må kanskje endre noe for å få deployet selv.

### Oppgave

* Fjerne hardkoding  av S3 bucket navnet ```app.py koden```, slik at den leser verdien "BUCKET_NAME" fra en miljøvariabel.
* Du kan gjerne teste APIet ditt ved å bruke kjell sine bilder  https://s3.console.aws.amazon.com/s3/buckets/kjellsimagebucket?region=eu-west-1
* Du skal opprette en GitHub Actions-arbeidsflyt for SAM applikasjonen. For hver push til main branch, skal
  arbeidsflyten bygge og deploye Lambda-funksjonen.
* Som respons på en push til en annen branch en main, skal applikasjonen kun bygges.
* Sensor vil lage en fork av ditt repository. Forklar hva sensor må gjøre for å få GitHub Actions workflow til å kjøre i
  sin egen GitHub-konto.

## B. Docker container

Python er ikke et veldig etablert språk i VerneVokterene, og du vil gjerne at utviklere som ikke har Python
installert på sin maskin skal kunne teste koden.

### Opppgave

Lag en Dockerfile som bygger et container image du kan bruke for å kjøre python koden.

Dockerfilen skal lages i mappen ```/kjell/hello_world```. Sensor skal kunne gjøre følgende kommando for å bygge et
container image og kjøre koden.

```shell
docker build -t kjellpy . 
docker run -e AWS_ACCESS_KEY_ID=XXX -e AWS_SECRET_ACCESS_KEY=YYY -e BUCKET_NAME=kjellsimagebucket kjellpy
```

Det ligger noen hint i filen app.py som vil hjelpe deg med å lage en ```Dockerfile```.

# Oppgave 2. Overgang til Java og Spring boot

Du innser raskt at Python ikke er veien videre for et konkurransedyktig produkt og har selv laget starten på en
Java-applikasjon som ligger i dette repoet. Applikasjonen er en Spring Boot applikasjon, som eksponerer et endepunkt

```http://<host>:<port>/scan-ppe?bucketName=<bucketnavn>```

Som du vil se bearbeider java-koden response fra tjenesten Rekognition litt mer en hva Python-varianten gjør.
En respons fra Java-applikasjonen kan se slik ut

```shell
{
    "bucketName": "kjellsimagebucket",
    "results": [
        {
            "fileName": "Man-in-PPE-kit-307511-pixahive.jpg",
            "violation": false,
            "personCount": 1
        },
        {
            "fileName": "almost_ppe.jpeg",
            "violation": false,
            "personCount": 1
        },
        {
            "fileName": "download.jpeg",
            "violation": true,
            "personCount": 1
        },
        {
            "fileName": "one_person_ppe.jpeg",
            "violation": false,
            "personCount": 1
        },
        {
            "fileName": "personnel-with-the-united-states-public-health-service-34a5d6-1024.jpg",
            "violation": false,
            "personCount": 2
        },
        {
            "fileName": "two_persons_one_no_ppe.jpeg",
            "violation": true,
            "personCount": 2
        }
    ]
}
```

Vi får tilbake ett JSON-objekt per fil i S3 Bucketen som inneholder følgende attributter

* Filename - Navnet på filen i S3 bucketen
* violation - true hvis det er person, eller personer på bildet uten nødvendig utstyr
* personCount - hvor mange personer Rekognition fant på bildet.

## A. Dockerfile

* Test java-applikasjonen lokalt i ditt cloud9 miljø ved å stå i rotmappen til ditt repository, og kjøre
  kommandoen ```mvn spring-boot:run```
* Du kan teste applikasjonen i en terminal med ```curl localhost:8080/scan-ppe?bucketName=<din bucket>``` og se på
  responsen.

### Oppgave

* Lag en Dockerfile for Java-appliksjonen. Du skal lage en multi stage Dockerfile som både kompilerer og kjører
  applikasjonen.

Sensor vil lage en fork av ditt repository, og skal kunne kjøre følgende kommandoer for å starte en docker container

```shell
docker build -t ppe . 
docker run -p 8080:8080 -e AWS_ACCESS_KEY_ID=XXX -e AWS_SECRET_ACCESS_KEY=YYY -e BUCKET_NAME=kjellsimagebucket ppe
```

## B. GitHub Actions workflow for container image og ECR

Du skal nå automatisere prosessen med å bygge/kompilere og teste Java-applikasjonen.
Lag en ny GitHub Actions Workflow fil, ikke gjenbruk den du lagde for Pythonkoden.

### Oppgave

* Lag en GitHub actions workflow som ved hver push til main branch lager og publiserer et nytt Container image til et
  ECR repository.
* Workflow skal kompilere og bygge et nytt container image, men ikke publisere image til ECR dersom branch er noe annet en main.
* Du må selv lage et ECR repository i AWS miljøet, du trenger ikke automatisere prosessen med å lage
  dette.
* Container image skal ha en tag som er lik commit-hash i Git, for eksempel: ```glenn-ppe:b2572585e```.
* Den siste versjonen av container image som blir pushet til ECR, skal i tillegg få en tag "latest".

# Oppgave 3- Terraform, AWS Apprunner og Infrastruktur som kode

Se på koden som ligger i infra katalogen, den inneholder kun en app_runner_service og en IAM roller som gjør denne i
stand til å gjøre API kall mot AWS Rekognition og lese fra S3.

## A. Kodeendringer og forbedringer

* Fjern hardkodingen av service_name, slik at du kan bruke ditt kandidatnummer eller noe annet som service navn.
* Se etter andre hard-kodede verdier og se om du kan forbedre kodekvaliteten.
* Se på dokumentasjonen til aws_apprunner_service ressursen, og reduser CPU til 256, og Memory til 1024 (defaultverdiene
  er høyere)

## B. Terraform i GitHub Actions

* Utvid din GitHub Actions workflow som lager et Docker image, til også å kjøre terraformkoden
* På hver push til main, skal Terraformkoden kjøres etter jobber som bygger Docker container image
* Du må lege til Terraform provider og backend-konfigurasjon. Dette har Kjell glemt. Du kan bruke samme S3 bucket
  som vi har brukt til det formålet i øvingene.
* Beskriv også hvilke endringer, om noen, sensor må gjøre i sin fork, GitHub Actions workflow eller kode for å få denne til å kjøre i sin fork.

# Oppgave 4. Feedback

## A. Utvid applikasjonen og legg inn "Måleinstrumenter"

I denne oppgaven får dere stor kreativ frihet i å utforske tjenesten Rekognition. Derw skal lage ny og relevant funksjonalitet.
Lag minst et nytt endepunkt, og utvid gjerne også den eksisterende koden med mer funksjonalitet.
Se på dokumentasjonen; https://aws.amazon.com/rekognition/

### Oppgave

* Nå som dere har en litt større kodebase. Gjør nødvendige endringer i Java-applikasjonen til å bruke Micrometer
  rammeverket for Metrics, og konfigurer  for leveranse av Metrics til CloudWatch
* Dere kan detetter selv velge hvordan dere implementerer måleinstrumenter i koden.

Med måleinstrumenter menes i denne sammenhengen ulike typer "meters" i micrometer rammeverket for eksempel;

* Meter
* Gauge
* Timer
* LongTaskTimer
* DistributionSummary

Dere skal skrive en kort begrunnelse for hvorfor dere har valgt måleinstrumentene dere har gjort, og valgene må  være relevante.
Eksempelvis vil en en teller som øker hver gang en metode blir kalt ikke bli vurdert som en god besvarelse, dette fordi denne
metrikkene allerede leveres av Spring Boot/Actuator.

### Vurderingskriterier

* Hensikten med å utvide kodebasen er å få flere naturlige steder å legge inn måleinstrumenter. Det gis ikke poeng for et stort kodevolum, men en god besvarelse vil legge til virkelig og nyttig funksjonalitet.
* En god besvarelse registrer både tekniske, og foretningsmessig metrikker.
* En god besvarelse bør bruke minst tre ulike måleinstrumenter på en god og relevant måte.

### B. CloudWatch Alarm og Terraform moduler

Lag en CloudWatch-alarm som sender et varsel på Epost dersom den utløses.Dere velger selv kriteriet for kriterier til at alarmen
skal løses ut, men dere  må skrive en kort redgjørelse for valget.

Alarmen skal lages ved hjelp av Terraformkode. Koden skal lages som en separat Terraform modul. Legg vekt på å unngå
hardkoding  av verdier i modulen for maksimal gjenbrukbarhet. Pass samtidig på at brukere av modulen ikke må sette mange
variabler når de inkluderer den i koden sin.

# Oppgave 4. Drøfteoppgaver

## Det Første Prinsippet - Flyt

### A. Kontinuerlig Integrering

Forklar hva kontinuerlig integrasjon (CI) er og diskuter dens betydning i utviklingsprosessen. I ditt svar,
vennligst inkluder:

- En definisjon av kontinuerlig integrasjon.
- Fordelene med å bruke CI i et utviklingsprosjekt - hvordan CI kan forbedre kodekvaliteten og effektivisere utviklingsprosessen.
- Hvordan jobber vi med CI i GitHub rent praktisk? For eskempel i et utviklingsteam på fire/fem utivklere?

### B. Sammenligning av Scrum/Smidig og DevOps fra et Utviklers Perspektiv

I denne oppgaven skal du som utvikler reflektere over og sammenligne to sentrale metodikker i moderne
programvareutvikling: Scrum/Smidig og DevOps. Målet er å forstå hvordan valg av metodikk kan påvirke kvaliteten og
leveransetempoet i utvikling av programvare.

### Oppgave

1. **Scrum/Smidig Metodikk:**

- Beskriv kort, hovedtrekkene i Scrum metodikk og dens tilnærming til programvareutvikling.
- Diskuter eventuelle utfordringer og styrker ved å bruke Scrum/Smidig i programvareutviklingsprosjekter.

2. **DevOps Metodikk:**

- Forklar grunnleggende prinsipper og praksiser i DevOps, spesielt med tanke på integrasjonen av utvikling og drift.
- Analyser hvordan DevOps kan påvirke kvaliteten og leveransetempoet i programvareutvikling.
- Reflekter over styrker og utfordringer knyttet til bruk av DevOps i utviklingsprosjekter.

3. **Sammenligning og Kontrast:**

- Sammenlign Scrum/Smidig og DevOps i forhold til deres påvirkning på programvarekvalitet og leveransetempo.
- Diskuter hvilke aspekter ved hver metodikk som kan være mer fordelaktige i bestemte utviklingssituasjoner.

#### Forventninger til Besvarelsen

- Din analyse bør være balansert, kritisk og godt underbygget med eksempler eller teoretiske argumenter.
- Reflekter over egne erfaringer eller hypotetiske scenarier for å støtte dine argumenter og konklusjoner.

### C. Det Andre Prinsippet - Feedback

Tenk deg at du har implementert en ny funksjonalitet i en applikasjon du jobber med. Beskriv hvordan du vil
etablere og bruke teknikker vi har lært fra "feedback" for å sikre at den nye funksjonaliteten møter brukernes behov.
Behovene Drøft hvordan feedback bidrar til kontinuerlig forbedring og hvordan de kan integreres i ulike stadier av
utviklingslivssyklusen.

## LYKKE TIL OG HA DET GØY MED OPPGAVEN!