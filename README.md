## Paraules claus
**RAG:** També conegut com Retrieval-Augmented Generation, es una tècnica que millora la qualitat del LLM permitint aprofitar recursos de dades adicionals sense necessitat de tornar a entrenar-los
**Fine-tuned:** Es el procès d'agafar un model ja entrenat i ajustar-lo per adaptarlo a fer tasques més especifiques
**Temperature:** Es un parametre per ajustar la longitud de la sortida del LLM

## Abans de provar la IA
Els requeriments de hardware en quant a GPU son els següents, per lo que no sería factible executar aquesta IA amb el portàtil del institut
- Minimum: NVIDIA RTX 3070 (8GB VRAM)
- Recommended: NVIDIA RTX 3090 (24GB VRAM)
- Optimal: 2x NVIDIA A100 (80GB VRAM)

La solució seria probarlo amb un *Inference Provider* utilitzant l'API de Huggingface.

## Com utilitzar l'API
1. Crear un compte de Huggingface
2. Anar a configuració del compte
3. Entrar a l'apartat de Tokens d'accés
4. Crear un token
5. Ficar el token en el script de Python

## Executar el script
~~~bash
# Clonar el repositori
git clone llmopt/asix1-practica1-JordiDragan
# Accedir a la carpeta
cd asix-practica1-JordiDragan
# Executar el script
python chat.py
~~~

## Provant la IA
L'hi he demanat que analitze el log d'Apache y m'ha donat el següent resultat:
> ChatCompletionOutputMessage(role='assistant', content='El log de Apache que se ha proporcionado muestra varios errores en tiempo de ejecución.\n\n1. El primero se refiere a una petición para el archivo favicon.ico, pero se encuentra que no existe en el directorio especificado. Es posible que no se haya creado o se hayan borrado los archivos en ese directorio.\n2. El segundo error es un Fatal PHP error "Uncaught Error: Call to undefined function mysql_connect()". Esto sugiere que la función mysql_connect() no está disponible en la versión de PHP que se está usando en el archivo index.php. La función mysql_connect() es retrocompatible y a partir de la versión 5.5.0 de PHP se ha quitado la utilización de la extensión MySQL para conectarse a bases de datos. Es necesario asegurarse de usar las National Shorthand Pointers (NSP) para conectarse a las bases de datos de MySQL como mysqli o PDO.\n3. El tercer error es "AH01630: client denied by server configuration". El usuario que realiza la petición ha sido negado por la configuración del servidor. Es posible que la cuenta del usuario no tiene los permisos adecuados, o que la configuración de firewall de apache o de la red bloquee la comunicación del cliente. Es necesario revisar la configuración del servidor.\n\nEs recomendable revisar los archivos del proyecto afectados y reparar los errores para que el servidor funcione correctamente.', tool_call_id=None, tool_calls=None)

## Diferències entre utilitzar l'API i descarregar el model
| Característica                    | API de Hugging Face                                                | Model local                                                 |
|-----------------------------------|--------------------------------------------------------------------|-------------------------------------------------------------|
| **Facilitat d’ús**                | Molt fàcil, només cal un token                                     | Requereix instal·lar dependències i el mòdel                |
| **Requisits de maquinari**        | Connexió a la xarxa                                                | Una GPU dedicada, minim de la serie 3000 de NVIDIA o similar|
| **Velocitat de resposta**         | Pot ser més lenta per la latència de xarxa o depenent del servidor | Depenent dels recursos de la màquina                        |
| **Cost**                          | Pot tenir cost segons l’ús                                         | Gratuït                                                     |
| **Personalització**               | Limitat al que ofereix l’API                                       | Totalment personalitzable (fine-tuning, temperature, etc.)  |
