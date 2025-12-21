# Active Localization - Object Localization using Deep Q-Network

Dự án triển khai hệ thống **Active Localization** sử dụng Deep Q-Network (DQN) để định vị đối tượng trong ảnh thông qua Reinforcement Learning.

## Bài toán

**Object Localization**: Tìm vị trí chính xác của một đối tượng trong ảnh (trả về bounding box).

## Tại sao Active Localization?

### Phương pháp truyền thống (2014-2015)

- **Region Proposals** (Selective Search, EdgeBoxes): Tạo hàng nghìn proposals → Chạy CNN cho mỗi proposal → Chọn box tốt nhất
- **Nhược điểm**: Tốn tính toán (2000+ forward passes/ảnh), không tận dụng thông tin tuần tự

### Ý tưởng Active Localization

Thay vì kiểm tra mọi vị trí, để agent **chủ động tìm kiếm** như con người:
1. Nhìn toàn ảnh → Phát hiện vùng có khả năng
2. Zoom/dịch chuyển → Điều chỉnh bounding box
3. Lặp lại cho đến khi đủ chính xác
4. Trigger → Dừng và trả về kết quả

**Ưu điểm**: Chỉ cần 1-40 forward passes thay vì hàng nghìn, tận dụng thông tin tuần tự, interpretable (xem được từng bước).

## Phương pháp

### Kiến trúc

- **Feature Extractor**: VGG16 pretrained (25,088 features)
- **DQN**: 
  - Input: Image features (25,088) + Action history (81) = 25,169 features
  - Output: Q-values cho 9 actions
- **9 Actions**: Trigger, Right, Left, Up, Down, Bigger, Smaller, Fatter, Taller

### Quá trình Inference

```
Bắt đầu với toàn ảnh (224x224)
    ↓
Mỗi step:
    1. Extract features từ vùng hiện tại
    2. Q-network → Chọn action tốt nhất
    3. Thực hiện action → Crop ảnh mới
    4. Cập nhật action history
    ↓
Lặp lại cho đến khi Trigger hoặc đạt 40 steps
    ↓
Trả về bounding box cuối cùng
```

### Training

- **Reward**: Dựa trên IoU improvement giữa các bước
- **Exploration**: Epsilon-greedy với guided exploration
- **Experience Replay**: Lưu transitions để học stable
- **Target Network**: Cập nhật định kỳ để stable Q-learning

## Cài đặt

```bash
pip install torch torchvision numpy matplotlib pandas pillow opencv-python imageio tqdm seaborn
```

## Sử dụng

### Training

```python
from utils.agent import *
from utils.dataset import *

# Load datasets
train_loader2012, val_loader2012 = read_voc_dataset(download=True, year='2012')
train_loader2007, val_loader2007 = read_voc_dataset(download=True, year='2007')

# Chuẩn bị datasets theo class
classes = ['cat', 'car', 'dog', 'aeroplane']
datasets_per_class = sort_class_extract([train_loader2007, train_loader2012])
datasets_eval_per_class = sort_class_extract([val_loader2007, val_loader2012])

# Training
for classe in classes:
    agent = Agent(classe, alpha=0.15, num_episodes=15, load=False)
    agent.train_validate(datasets_per_class[classe], 
                        datasets_eval_per_class[classe], 
                        classe)
```

### Prediction

```python
agent = Agent(classe, load=True)
image, gt_boxes = extract(index, dataset)
predicted_box = agent.predict_image(image, plot=True)  # plot=True tạo GIF animation
```

## Dataset

PASCAL VOC 2007 & 2012 với 20 classes.

## Kết quả

- Models: `models/q_network_{class}`
- Logs: `logs_over_epochs.csv`
- Visualizations: `media/movie_*.gif` (animations của quá trình localization)

## Tác giả

Dự án được phát triển cho môn học CS106 - 22520465
