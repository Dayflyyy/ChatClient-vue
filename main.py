from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins, you can set specific origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Model for request body
class Message(BaseModel):
    text: str

@app.post("/test/", response_model=dict)
async def analyze_eye_image_chat(message: Message):
    # Here you can process the received message
    # For now, let's just echo back the received message
    return {"message": message.text}

@app.options("/test/", response_model=dict)
async def get_options():
    return {"methods": ["POST"]}


# @app.post("/analyze-eye-image/")
# async def analyze_eye_image(file: UploadFile = File(...), question: str = Form(...)):
#     # 保存上传的文件
#     contents = await file.read()
#     temp_dir = 'temp'
#     if not os.path.exists(temp_dir):
#         os.makedirs(temp_dir)
#     file_path = os.path.join(temp_dir, file.filename)
#     with open(file_path, 'wb') as f:
#         f.write(contents)

#     # 处理图像并获取FLAIR输出的函数
#     disease_probs = await classify_disease(f'temp/{file.filename}')
#     disease_level = await diagnose_disease_level(disease_probs)
#     segmentation_image_path = await segment_disc(f'temp/{file.filename}')

#     # 构建Prompt并调用LLM生成诊断报告
#     # prompt = (await construct_sys_prompt(disease_probs, disease_level)).append(await construct_user_prompt(question))
#     prompt_sys = await construct_sys_prompt(disease_probs, disease_level)
#     prompt_user = await construct_user_prompt(question)
#     prompt_sys.append(prompt_user)
#     diagnosis_report = await generate_diagnosis_report(prompt_sys)

#     # 返回结果
#     return JSONResponse(content={
#         "disease_probabilities": disease_probs,
#         "disease_level": disease_level,
#         "segmentation_image": segmentation_image_path,
#         "prompt": prompt_sys,
#         "diagnosis_report": diagnosis_report
#     })
    


# async def classify_disease(image_path):
#     # 调用疾病分类模型
#     # 定义图像路径和文本标签
#     # image_path = "./documents/severe_nonprol_dr.jpg"
#     text_labels = ["normal", "healthy", "macular edema", "diabetic retinopathy", "glaucoma", "macular hole",
#                    "lesion", "lesion in the macula"]

#     # 调用函数
#     probs, logits = classify_image(image_path, text_labels)

#     # 确保 probs 和 logits 是 Python 列表
#     precision = 4
#     # 确保 probs 和 logits 是 Python 列表并四舍五入到四位小数
#     # 如果 probs 和 logits 是嵌套列表，您需要对内部列表进行四舍五入
#     probs_list = [float(round(prob, precision)) for prob in (
#         probs.tolist() if isinstance(probs, np.ndarray) else probs)]
#     logits_list = [float(round(logit, precision)) for logit in (
#         logits.tolist() if isinstance(logits, np.ndarray) else logits)]
#     return {
#         "probs": {label: prob for label, prob in zip(text_labels, probs_list)},
#         "logits": {label: logit for label, logit in zip(text_labels, logits_list)}
#     }
#     # return {"glaucoma": 0.8, "diabetic_retinopathy": 0.2}


# async def diagnose_disease_level(disease_probs):
#     # 基于疾病概率进行病程度判断的逻辑
#     return "mild"


# async def segment_disc(image_path):
#     # 这里应该是调用视杯视盘分割模型的代码
#     return "path/to/segmented_image.jpg"


# async def find_most_likely_disease(disease_probs: Dict[str, Dict[str, float]]) -> Tuple[str, float]:
#     # ["normal", "healthy", "macular edema", "diabetic retinopathy", "glaucoma", "macular hole",
#     #     "lesion", "lesion in the macula"]
#     # 根据模型输出构建用于生成诊断报告的Prompt
#     disease_prob_dict: Dict[str, float] = disease_probs['probs']
#     most_likely_item: Tuple[str, float] = ('', 0.0)
#     most_likely_item: Tuple[str, float] = max(
#         disease_prob_dict.items(), key=lambda item: item[1])

#     return most_likely_item


# async def construct_sys_prompt(disease_probs: Dict[str, Dict[str, float]], disease_level: Dict[str, Dict[str, float]])\
#         -> List[Dict[str, str]]:
#     # most_likely_disease=find_most_likely_disease(disease_probs,disease_level)#Tuple:(disease,probility)
#     disease_prob_dict = disease_probs['probs']
#     sys_role_setting_postive = '我希望你充当专业的眼科医生的角色，对眼科领域有着非常丰富而且专业的知识，你需要根据我提供给你的患各种眼科疾病的概率数值大小用中文作出诊断，\
#         在我传递给你的disease_probabilities列表中 数值越大表示换这种病的可能性越大，你需要根据这个列表判断出患哪种疾病的可能性最大，并且据此从该疾病的基本症状，诊断方法，治疗方法几个方面给出治疗意见。'
#     sys_role_setting_negative = '在回答中，尽量不要出现具体的数值，而采用定性的描述。并且不要提到我有给你提供了患眼科疾病的概率数值大小的情况。'
#     sys_prompt: List[Dict[str, str]] = [
#         {"role": "system", "content": f"{sys_role_setting_postive},已知各个疾病的患病概率是{disease_prob_dict},请你注意{sys_role_setting_negative}"},
#     ]

#     return sys_prompt
#     # return "Based on the analysis..."


# async def construct_user_prompt(question: str)\
#         -> Dict[str, str]:
#     user_prompt = {"role": "user", "content": f"你好！{question}"}
#     return user_prompt


# async def generate_diagnosis_report(prompt):
#     # 使用await来调用异步函数
#     chat_api_response = await call_chat_api(prompt)
#     return chat_api_response
