# projects-with-OpenAI-API
Use Case Development 
In software engineering, an illustration of a system's essential to operation from the viewpoint of its users is called a use case model. It depicts the communications between users (actors) and the system as they work together to complete tasks or goals. The desired behavior of a system is captured and documented using use case modelling, which is frequently used in the fields of software development and engineering systems. In this training program we are to develop 2 Use Case models. The given models in OpenAI training: -
1) Use Case –Fraudulent E-mail Detection
2) Use Case –Medical Condition Detection
3) Sentiment Analysis of Company review
Dataset Preparation for each use case: -
1)	Use Case –Fraudulent E-mail Detection 
My dataset represents a mail and then the AI deciphering whether it is fraud or not. Prompt gives the mail.
Completion explains whether it is fraud or not fraud.
First install OpenAI and when successfully installed import.
Creating the balanced training data for fraud mail detection: -
Let’s create a JSONL file
Getting a csv file from the JSONL file
2)	Use Case –Medical Condition Detection
My dataset represents symptoms and diagnosis.
Prompt represents the symptoms that the user is experiencing.
Completion is where the system gives response with the medical condition the user might be suffering from and also recommends for appointment with a concerned medical practitioner.
Creating the balanced training data for medical condition detection: -  
Next, we create a JSONL file. We can also get a csv file the same way
3)	Dataset Preparation for Sentiment Analysis of Company review
This dataset have been made by keeping in mind that the prompt will have more than just the  review being provided.
Prompt has EID that is Employee ID and it has the review given by the very employee.
Completion tries to understand the sentiments of the employee.
First, we create a dataset that has both positive and negative reviews: -
 The next step is to create a JSONL file
Again if you want then you can create a csv file for it too
 Making use of Prompt Engineering with ChatGPT: -
Even when using prompt engineering to create datasets, chatgpt might not always be able to handle each specification. What I experienced was: -
•	the suffix missing
•	the stopping sequence
•	The white space before the completion that is 
“completion”: “ the......\n”
•	The balance between the appropriate and the fraudulent mails in the dataset.
FINE-TUNING THE USE CASE MODELS: -
Fine-tuning is an immersive process and as of now has different methods, but I have used the API method, using command lines, etc.
We will understand fine_tuning with one of the use case models in a more elaborate manner but I will also include the other fine-tuned models.
Let us learn step by step with Sentiment Analysis of Company review
1.	You need to have a prepared JSONL file of your dataset. We have already followed the necessary steps for the creation of dataset and JSONL type file.

 
2.	Verifying whether the file is ready to finetune or any changes need to be made in the prompts and completions
A.	An exclamation point ('!') at the start of a command in many programming languages designates that the cmd ought to be performed in the system shell or command-line terminal instead of in the present language being utilised.
B.	openai: This section relates to the OpenAI tools library, which is a tool for the command-line made available by OpenAI to help with specific tasks involving artificial intelligence or natural language processing.
C.	Utilities prepare_data.fine_tune: This is a particular subcommand or feature offered by the OpenAI tools library. It tends to be employed in this situation to prepare facts for adjusting an artificial intelligence model.
D.	This component of the instruction is a command-line argument: "-f fraud_training_data.jsonl". The training data file can be specified by using the "-f" flag. The 'training_data.jsonl' file in this instance is offered as the input information during the fine-tuning procedure. The file's '.jsonl' extension denotes that it is in JSON Lines format, a text-based style wherein each sentence contains a legitimate JSON entity.

 
3.	 Uploading the file
A.	openai.File.create(...) when upload_response is true: This line uses the OpenAI API to create a file upload request. To begin the upload process, it is utilising the openai.File.create function. To indicate the file that needs to be transmitted and the goal for the the upload, the method requires settings
B.	The file to upload is identified in this section of the code by file=open (file_name, "rb"). The binary mode ("rb") file named file_name is opened using the open () method.
C.	The objective of the document's uploading is determined by the code's purpose='fine-tune'. The fact that the objective in this example is 'fine-tune' indicates the file is meant to be used for fine-tuning an artificial intelligence model.
D.	'file_id' equals 'upload_response'.id: The upload_response object includes details about the uploaded file, including its ID, when the file is successfully uploaded. The id parameter is taken out of the upload_response object and put into the value of the variable file_id in this line of code.
E.	The upload_response object, which could include information like the submitted file's ID, name, URL, etc., is merely output or returned by this portion of the code.
F.	This code generates an upload_response response object from the OpenAI API that contains details about the submitted file. Details like the file's ID (stored in file_id), title, URL, dimensions, and additional metadata could be contained in the upload_response. The API implementation and the data that OpenAI returns will determine the data made accessible in the response.
G.	Normally, once this programme executes efficiently, one can return to and retrieve the file that was uploaded using the file_id for additional processing, such as utilising it as training data to optimise an artificial intelligence model. The precise application and subsequent actions are contingent upon the larger context and goal provided by the code.

 
4.	After getting the file-id, we use this command to request fine-tuning.
A.	openai is fine_tune_response.FineTune.create(...): This line starts the process of fine-tuning a pre-trained language model via the OpenAI API. It utilises OpenAI.To begin the fine-tuning process, use the FineTune.create function.
B.	training_file="file-424eOUdVWuRXcXkSjKp2nENN": The training_file argument is set to "file-424eOUdVWuRXcXkSjKp2nENN" in this section within the code. The ID or address of the file containing the training data is specified by this option. The OpenAI API was probably utilised for uploading the file containing this ID in the past (as was described in the preceding code line description).
C.	Model parameter is set to "davinci" in this section of the code. Another among the pre-trained language models offered by OpenAI is the davinci engine. The technique of fine-tuning involves taking a pre-trained model and refining it on unique data to adjust it for a particular purpose.
D.	The response object (fine_tune_response) obtained via the OpenAI API, that includes details about the fine-tuning procedure, is the outcome of the above code. The fine-tuning job status, the model used, the training data, the time required, and any faults or correspondence detected throughout the fine-tuning procedure can all be incorporated in the fine_tune_response's payload.
E.	The API execution and the data that OpenAI returns will determine the precise data available in the response. It might contain details like the ID of the modified model, the state of its training, its completion, along with additional pertinent data.\

 
5.	Following the effective completion of this code being used, one would take advantage of the data in fine_tune_response to track the advancement of the fine-tuning task and retrieve the tweaked model for later use.
A.	The details provided by the OpenAI API in relation to the requested fine-tuning job will be contained in the retrieve_response object. The state of the fine-tuning work, the trained model's ID, the training data used, the time required, assessment metrics, any mistakes found, and other pertinent information regarding the fine-tuning procedure can all be contained in the data portion of the retrieve_response object.
 
B.	"object": "fine-tune-event" "Fine-tune-event" is the value connected to the key "object". This suggests that the reported incident has something to do with the finetuning procedure.
C.	"level": "info": "info" is the value corresponding to the key "level." This describes the occurrence or message's seriousness or level. It is a message of instruction in this instance, indicating that it offers beneficial details without pointing out any shortcomings or faults.
D.	"message": "Fine-tune succeeded" The value "Fine-tune succeeded" is linked to the key "message". This signals that the method of fine-tuning was effective and is the actual substance of the ensuing message. It confirms that no major stumbles occurred during the fine-tuning process.
E.	"created_at" 1690991824 The value 1690991824 is assigned to the key "created_at". This shows the timing for the creation of the corresponding message. The value is a Unix timestamp, or Epoch time, and it represents the duration in seconds since January 1st, 1970 (UTC).

Now that we are done with finetuning, we need to check whether the model responds efficiently
