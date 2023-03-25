import requests

url = "https://personalized-brand.api.rephrase.ai/v2/campaign/create"

payload = {
    "videoDimension": {
        "height": 1080,
        "width": 1920
    },
    "scenes": [{"elements": [
                {
                    "style": {
                        "height": "100%",
                        "width": "100%",
                        "position": "absolute",
                        "zIndex": 1
                    },
                    "asset": {
                        "kind": "Image",
                        "use": "Background",
                        "url": "https://imgix.elitedaily.com/uploads/image/2020/3/24/f4869313-aba5-403c-b554-e57329cbc3a0-austin-distel-wawefydpkag-unsplash.jpg"
                    }
                },
                {
                    "style": {
                        "position": "absolute",
                        "zIndex": 2,
                        "bottom": "0em",
                        "objectFit": "cover",
                        "height": "37.5em",
                        "width": "66.66666666666667em",
                        "left": "16.666666666666664em"
                    },
                    "asset": {
                        "spokespersonVideo": {
                            "output_params": {"video": {
                                    "resolution": {
                                        "height": 720,
                                        "width": 1280
                                    },
                                    "background": {"alpha": 0},
                                    "crop": {"preset": "MS"}
                                }},
                            "model": "danielle_pettee_look_2_nt_aug_2022",
                            "voiceId": "7bc739a4-7abc-46db-bc75-e24b6f899fa9__005",
                            "gender": "female",
                            "transcript": "<speak>Hello Everyone! My Name is Anush Gupta I am from Mechanical currently I am in a 3rd Year and I am an AI enthusiast</speak>",
                            "transcript_type": "ssml_limited"
                        },
                        "kind": "Spokesperson"
                    }
                },
                {
                    "style": {
                        "variant": "subheading",
                        "fontSize": "4.777777777777778em",
                        "fontFamily": "Roboto",
                        "color": "#FFFFFF",
                        "position": "absolute",
                        "zIndex": 15,
                        "align": "left",
                        "height": "5.912361095419285em",
                        "width": "30.170754733240013em",
                        "bottom": "33.28846002860913em",
                        "left": "12.064089036806962em",
                        "fontColor": "#631111",
                        "textDecorationColor": "#631111"
                    },
                    "asset": {
                        "textStyle": {
                            "fontColor": "#631111",
                            "fontSize": "4.777777777777778em",
                            "textDecorationColor": "#631111"
                        },
                        "kind": "Text",
                        "text": "Title Text"
                    }
                }
            ]}],
    "title": "16:9 Widescreen",
    "thumbnailUrl": "https://rephrase-assets.s3.ap-south-1.amazonaws.com/template_thumbnails/cold_reachout_1.png"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)