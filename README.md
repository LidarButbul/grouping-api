# Claim Grouping API

This project provides a FastAPI application that groups legal claims into clusters using K-Means clustering. The project leverages Sentence-BERT (SBERT) to generate embeddings for the claims and uses these embeddings for clustering.

## Features

- **Sentence-BERT**: Generates high-quality sentence embeddings for the claims.
- **K-Means Clustering**: Groups claims into clusters based on similarity.
- **API Endpoints**: Provides endpoints to submit claims and receive cluster groupings.

## Requirements

- Python 3.7 or higher
- Install the required Python packages using the instructions below.

 **Note:** This project requires NumPy version 1.x due to compatibility issues with some dependencies. The `requirements.txt` file ensures that the correct version of NumPy is installed.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/LidarButbul/grouping-api.git
    cd grouping-api
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Start the FastAPI application:**

    ```bash
    uvicorn app:app --reload
    ```
 **Note:** Starting the application might take a bit of time. Please be patient and wait for the message `Application startup complete` to appear in the terminal before trying to access the site.
 
The application will be available at `http://127.0.0.1:8000`.

2. **Interact with the API:**

   You can access the interactive API documentation by navigating to:

    ```
    http://127.0.0.1:8000/docs
    ```

    Use the documentation to test the endpoints. For example, you can submit claims to the `/group` endpoint and receive clustered groupings as a response.

## Example Request

```json
{
  "claims": [
    "A wireless telephone apparatus comprising: a handset; an onioff-hook switch; a wireless communications module for establishing first and second cellular telephone calls via a base station; and means for generating an explicit call transfer command for sending to the base station in response to activation of the on-hook switch when the first and second wireless calls are established through the apparatus.",
    "The apparatus of claim 1, ftirther comprising a body having a cradle for the handset, wherein the onloff hook switch operates in response to placing the handset in the cradle.",
    "The apparatus of claim 1, 2 or 3, ftirther comprising: call receiving means for receiving a first call from a calling party; call initiating means for entering a call initiation mode, in response to activation of a f irst predetermined button, for initiating a second call; and transfer means for putting the first call on hold, initiating the second call, and toggling, in response to activation of the first predetermined button, between the first and second calls.",
    "The apparatus of claim 3, wherein the first predetermined button is a redial button.",
    "The apparatus of claim 3 or 4, wherein the transfer means toggles between the first and second calls by putting either the first or the second call on hold.",
    "The apparatus of any one of claims 3 to 5, further comprising means for enabling a phonebook lookup operation when in the call initiation mode.",
    "The apparatus of any one of claims 3 to 6, wherein the call initiation mode and a dialling mode are entered using the first predetermined button.",
    "The apparatus of any one of the preceding claims, further comprising display means for displaying first and second icons adjacent information relating to the first and second calls respectively, the first and second icons being adapted to switch when toggling between calls.",
    "The apparatus of claim 8, further comprising selection means for selecting information displayed on the display means.",
    "The apparatus of claim 8 or 9, wherein the transfer means is adapted to initiate a call to a second party whose information is displayed on the display means.",
    "The apparatus of any one of claims 3 to 10, further comprising a second predetermined button which ends an active call and reverts to a call on hold.",
    "The apparatus of claim 11, wherein the second predetermined button is a clear button.",
    "A method of effecting a call transfer comprising: establishing first and second cellular telephone calls at a wireless telephone apparatus, and generating an explicit call transfer command for sending to a base station in response to activation of the on-hook switch.",
    "A communication apparatus as substantially herein before described with reference to the accompanying drawings in Figures 1 to 7."
  ],
  "n_clusters": 4
}
