import os
import time
import logging
from PIL import Image

# 配置日志记录器
logging.basicConfig(
    level=logging.INFO,  # 设置日志级别，可以选择 DEBUG、INFO、WARNING、ERROR、CRITICAL 等级别
    filename='debug.log',  # 指定日志文件名称
    format='%(asctime)s [%(levelname)s]: %(message)s',  # 指定日志格式
    datefmt='%Y-%m-%d %H:%M:%S'  # 指定日期时间格式
)


# def transparent_image(image_path, alpha_value):
#   # 打开要处理的图片
#   image = Image.open(image_path)

#   # 创建一个具有透明度通道的新图片
#   image_with_alpha = image.convert('RGBA')

#   # 设置透明度（alpha通道），0表示完全透明，255表示完全不透明
#   alpha_value = 64  # 128 表示半透明
#   width, height = image_with_alpha.size

#   # 遍历每个像素，并设置透明度
#   for x in range(width):
#       for y in range(height):
#           r, g, b, a = image_with_alpha.getpixel((x, y))
#           image_with_alpha.putpixel((x, y), (r, g, b, alpha_value))

#   # 保存包含透明度的图片
#   # image_with_alpha.save('output_image.png')

#   # 显示结果
#   # image_with_alpha.show()
#   return image_with_alpha

# # 打开第一张图片作为背景
# # background_image = Image.open('./image/IMG_0859.PNG')
# background_image = transparent_image('./image/IMG_0859.PNG', 128)

# # 初始化一个空的大图
# x_extend = 2
# y_extend = 2
# width, height = background_image.size
# background_image = background_image.resize((width * x_extend, height * y_extend), Image.ANTIALIAS)

# final_image = Image.new('RGBA', (x_extend * width, y_extend * height))

# # 打开其他图片并等比例缩小后依次拼接
# image_paths = ['./image/IMG_0859.PNG', './image/IMG_0865.PNG', './image/IMG_0866.PNG',
#   './image/IMG_0859.PNG']  # 替换为您的图片路径

# for i in range(x_extend):
#   for j in range(y_extend):
#     image_path = image_paths[i*y_extend + j]
#     print(image_path)
#     img = Image.open(image_path)
#     img_width, img_height = img.size
#     # 计算等比例缩小后的新尺寸
#     new_width = width
#     new_height = int(img_height * (width / img_width))
#     # 缩小图片
#     img = img.resize((new_width, new_height), Image.ANTIALIAS)
#     # 将缩小后的图片粘贴到大图上
#     print("offset : ", i * x_extend, j * y_extend)
#     final_image.paste(img, (i * width, j * height))

# result_image = Image.alpha_composite(final_image, background_image)
# # 保存生成的大图
# result_image.save('final_image.png')

# # 显示生成的大图
# result_image.show()

class MergeImage:
    def __init__(self, image_background_path, alpha_value, image_folder, x_extend, y_extend):
        self.image_background_path = image_background_path
        self.alpha_value = alpha_value
        self.image_folder = image_folder
        self.x_extend = x_extend
        self.y_extend = y_extend
        self.trans_jpg()
        time.sleep(1)

    def trans_jpg(self):
      # 指定文件夹路径
      folder_path = self.image_folder  # 替换为您的文件夹路径

      # 遍历文件夹中的所有文件
      for filename in os.listdir(folder_path):
          source_path = os.path.join(folder_path, filename)
          logging.info("filename {0}".format(source_path))
          # 检查文件是否为图像文件（可以根据需要添加其他扩展名）
          if not filename.lower().endswith(('.png', '.jpeg', '.jpg', '.gif', '.bmp', '.tiff', '.heic')):
              continue

          # 构造新的文件名（将原文件的扩展名改为.jpg）
          new_filename = os.path.splitext(filename)[0] + '.jpg'
          new_path = os.path.join(folder_path, new_filename)
          logging.info("rename {0} to {1}".format(source_path, new_path))
          # 重命名文件
          os.rename(source_path, new_path)

    def composite_image(self):
      background_image = self.transparent_image()
      background_image.save('./output/background_image.png')
      logging.debug("save background_image")
      logging.debug("background_image.size : {}".format(background_image.size))
      # background_image.size : (1170, 2532)

      concat_image = self.concat_image()
      concat_image.save('./output/concat_image.png')
      logging.debug("save concat_image")
      # concat_image.size : (2340, 5064)
      logging.debug("concat_image.size : {}".format(concat_image.size))

      result_image = Image.alpha_composite(concat_image, background_image)
      result_image.save('./output/final_image.png')
      logging.debug("save result_image")

    def transparent_image(self):
        # 打开要处理的图片
        image = Image.open(self.image_background_path)
        # 创建一个具有透明度通道的新图片
        image_with_alpha = image.convert('RGBA')

        # 设置透明度（alpha通道），0表示完全透明，255表示完全不透明
        alpha_value = self.alpha_value  # 128 表示半透明
        width, height = image_with_alpha.size

        # 遍历每个像素，并设置透明度
        for x in range(width):
            for y in range(height):
                r, g, b, a = image_with_alpha.getpixel((x, y))
                image_with_alpha.putpixel((x, y), (r, g, b, alpha_value))

        # 保存包含透明度的图片
        # image_with_alpha.save('output_image.png')
        # 显示结果
        # image_with_alpha.show()
        image_with_alpha = image_with_alpha.resize((width * self.x_extend, height * self.y_extend)
          , Image.ANTIALIAS)
        return image_with_alpha
    
    def concat_image(self):
      # 使用os模块获取文件夹中的所有文件名
      image_path = []

      for root, dirs, files in os.walk(self.image_folder):
          for file in files:
            # if self.image_background_path == os.path.join(root, file):
            #   continue
            if not file.lower().endswith(('.png', '.jpeg', '.jpg', '.gif', '.bmp', '.tiff', '.heic')):
              continue
            image_path.append(os.path.join(root, file))

      # 图片数量不够的话 直接退出
      logging.info("image number : {0}".format(len(image_path)))
      assert len(image_path) >=  self.x_extend * self.y_extend

      # 打印文件名列表
      for file_name in image_path:
        logging.debug("image path : {}".format(file_name))

      # 获取背景照片的大小
      with Image.open(self.image_background_path) as bk_image:
        self.bkimg_width, self.bkimg_height = bk_image.size

      concat_image = Image.new('RGBA', (self.x_extend * self.bkimg_width, self.y_extend * self.bkimg_height))
      image_path = image_path[:self.x_extend * self.y_extend]

      # 打开其他图片并等比例缩小后依次拼接
      for i in range(self.x_extend):
        for j in range(self.y_extend):
          little_image = image_path[i*self.y_extend + j]
          logging.debug("concat image {}".format(little_image))
          img = Image.open(little_image)
          img_width, img_height = img.size

          # 计算等比例缩小后的新尺寸
          new_width = img_width
          new_height = int(img_height * (self.bkimg_width / img_width))
          # 缩小图片
          img = img.resize((new_width, new_height), Image.ANTIALIAS)

          # 将缩小后的图片粘贴到大图上
          concat_image.paste(img, (i * self.bkimg_width, j * self.bkimg_height))

      return concat_image

forNaNa = MergeImage(
  image_background_path="./image/IMG_0784.jpg",
  alpha_value=128,
  image_folder="./image_test",
  x_extend=2,
  y_extend=2
)
forNaNa.composite_image()