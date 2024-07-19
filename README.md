 # Using DQN on Computer Vision 
 ![ex0](https://raw.githubusercontent.com/hoanglvuit/Active-Object-Localization-with-Deep-Reinforcement-Learning/main/realmedia/movie_0.gif)
 ## Abstract 
- Active-Object-Localization là một trong những problem lâu đời và nền tảng của việc áp dụng Reinforcement Learning vào Computer Vision.
- Một cách tiếp cận cơ bản đối với những bài toán object localization (object detection):
+ Train một CNN dùng để phân loại
+ Apply phương pháp sliding windown trên một tấm ảnh để cắt thành nhiều phần phẩn nhỏ
+ Đưa chúng vào pretrained CNN bên trên để phân loại
+ Kết hợp tất cả result ta sẽ localize được object
- Để có kết quả tốt, ta sẽ phải cắt thành nhiều phần và sẽ có rất nhiều phần dược đưa vào pretrained CNN.
- Việc áp dụng RL cụ thể là DQN sẽ giúp giảm bớt số lượng ảnh đưa vào CNN -> cải thiện về mặt thời gian
- Đơn giản là train một agent để nó hiểu tiếp theo nó sẽ transform như thế nào để cải thiện độ chính xác. Cụ thể theo như paper sau: [object_localization](https://arxiv.org/abs/1511.06015)
## How to use 
- Vì phải sử dụng gpu nên chúng ta sẽ train trên một số platform miễn phí gpu như colab.
- Ở đây, mình sử dụng kaggle - vì nó hỗ trợ gpu trong thời gian đủ dài để train.
- Sử dụng giống file run_onkaggle
- Hoặc clone về local rồi push lên github -> clone về kaggle
- Nên điều chỉnh file training và visualize nếu gặp lỗi.
- Tham khảo original tại: [lz](https://github.com/rayanramoul/Active-Object-Localization-Deep-Reinforcement-Learning/tree/master)
## Conclusion
- Good look
- If it's helpful, please give me the star :D 
 
