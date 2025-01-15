import torch
print(torch.cuda.is_available())  # True여야 정상
print(torch.cuda.device_count())  # 1 이상이어야 정상
print(torch.cuda.get_device_name(0))  # GPU 이름 확인
