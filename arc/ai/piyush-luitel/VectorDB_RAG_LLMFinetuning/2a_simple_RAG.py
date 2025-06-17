import ollama  # Import the Ollama Python client for interacting with local models

# Load the dataset from a text file
dataset = []
with open('cat-facts.txt', 'r') as file:  # Open the file in read mode
    dataset = file.readlines()            # Read all lines into a list (each line is a fact or chunk)
    print(f'Loaded {len(dataset)} entries')  # Print how many entries (chunks) were loaded

# Set the model names (Note: these hf.co models don't work directly with Ollama!)
# You should replace these with models pulled via `ollama pull` from https://ollama.com/library
EMBEDDING_MODEL = 'hf.co/CompendiumLabs/bge-base-en-v1.5-gguf'  # Placeholder for embedding model
LANGUAGE_MODEL = 'hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF'    # Placeholder for language model

# VECTOR_DB will store (chunk, embedding_vector) pairs
VECTOR_DB = []

# Function to embed a chunk and add it to the database
def add_chunk_to_database(chunk):
    # Generate embedding vector for the chunk using the specified model
    embedding = ollama.embed(model=EMBEDDING_MODEL, input=chunk)['embeddings'][0]
    # Add the chunk and its embedding to the VECTOR_DB
    VECTOR_DB.append((chunk, embedding))

# Loop through each chunk and add it to the vector database
for i, chunk in enumerate(dataset):
    add_chunk_to_database(chunk)  # Add the chunk to VECTOR_DB
    print(f'Added chunk {i+1}/{len(dataset)} to the database')  # Print progress

# Function to compute cosine similarity between two vectors
def cosine_similarity(a, b):
    dot_product = sum([x * y for x, y in zip(a, b)])  # Compute dot product
    norm_a = sum([x ** 2 for x in a]) ** 0.5          # Compute norm (magnitude) of vector a
    norm_b = sum([x ** 2 for x in b]) ** 0.5          # Compute norm (magnitude) of vector b
    return dot_product / (norm_a * norm_b)            # Return cosine similarity

# Function to retrieve top_n similar chunks given a query
def retrieve(query, top_n=3):
    # Generate embedding vector for the query
    query_embedding = ollama.embed(model=EMBEDDING_MODEL, input=query)['embeddings'][0]
    similarities = []  # Temporary list to store (chunk, similarity) pairs

    # Calculate similarity between query and each chunk
    for chunk, embedding in VECTOR_DB:
        similarity = cosine_similarity(query_embedding, embedding)  # Cosine similarity
        similarities.append((chunk, similarity))  # Add to list

    # Sort by similarity in descending order (most similar first)
    similarities.sort(key=lambda x: x[1], reverse=True)
    # Return top_n most similar chunks
    return similarities[:top_n]

# --------- Chatbot interaction starts here ---------

# Take user input as a question
input_query = input('Ask me a question: ')

# Retrieve the most relevant context chunks using the retrieval function
retrieved_knowledge = retrieve(input_query)

# Print the retrieved chunks and their similarity scores
print('Retrieved knowledge:')
for chunk, similarity in retrieved_knowledge:
    print(f' - (similarity: {similarity:.2f}) {chunk}')

# Build the system prompt using retrieved knowledge
instruction_prompt = f'''You are a helpful chatbot.
Use only the following pieces of context to answer the question. Don't make up any new information:
{'\n'.join([f' - {chunk}' for chunk, similarity in retrieved_knowledge])}
'''

# Send prompt and user message to the language model using streaming
stream = ollama.chat(
    model=LANGUAGE_MODEL,
    messages=[
        {'role': 'system', 'content': instruction_prompt},  # Context/instructions
        {'role': 'user', 'content': input_query},           # User query
    ],
    stream=True,  # Enable streaming response
)

# Print the chatbot's response in real-time as it's generated
print('Chatbot response:')
for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)
