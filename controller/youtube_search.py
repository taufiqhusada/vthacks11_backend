from googleapiclient.discovery import build
from pprint import PrettyPrinter
from youtube_transcript_api import YouTubeTranscriptApi
from config.openai_connector import init_openai_config

def get_summary_from_transcript(transcript, config):
    openai = init_openai_config(config['openai_api_key'])

    prompt = f"""You have been tasked with creating a concise summary of a
                YouTube video using its transcription.Make a summary of the transcript.
                Create 10 bullet points that summarize the key points or important moments from the video's
                transcription.In addition to the bullet points, extract the most important keywords and any
                complex words not known to the average reader aswell as any acronyms mentioned. For each keyword
                and complex word, provide an explanation and definition based on its occurrence in the transcription.
                Please ensure that the summary, bullet points, and explanations fit within the 500-word limit, while still
                offering a comprehensive and clear understanding of the video's content. Use the given transcript delimited by triple backticks:
                transcript: ```{transcript}```"""

    response = openai.ChatCompletion.create(
    model=config['openai_model'],
    messages=[
        {
        "role": "user",
        "content": prompt
        },
    ],
    )

    return response["choices"][0]["message"]["content"]    

def get_transcript(video_id_list, config):
    transcript_list, unretrievable_videos = YouTubeTranscriptApi.get_transcripts(video_id_list, continue_after_error=True)

    transcript_dict={}
    cnt = 0
    for video_id in transcript_list.keys():  
        srt = transcript_list.get(video_id)
        text_list = []
        for i in srt:
            text_list.append(i['text'])
        full_transcript = (' ').join(text_list)[0:75000]

        transcript_dict[video_id]= get_summary_from_transcript(full_transcript, config)
        
        break
    return transcript_dict

def get_video_links_by_keyword(keyword, config):
    youtube = build('youtube','v3',developerKey = config['youtube_api_key'])
    # print(type(youtube))
    request = youtube.search().list(q=keyword, part='id',type='video', maxResults=10)
    res = request.execute()

    id_list = []
    for i in res['items']:
        id_list.append(i['id']['videoId'])

    return id_list


