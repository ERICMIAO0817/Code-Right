<template>
<div id="htmlWrap" style="background:none;">
	  <!--header-->
	  <div class="bg545C64" style="background:none;box-shadow:0 0 3px #e5e5e5;">
		<HrIndexMenuVue></HrIndexMenuVue>
	  </div>

    <!-- 轮播图 -->
    <div class="bannerWrap" style="width:100%;height:842px;">
      <!-- https://www.swiper.com.cn/demo/220-effect-fade.html -->

      <!-- Swiper -->
      <div class="swiper-container">
        <div class="swiper-wrapper">
          <div class="swiper-slide" ><img src="../assets/image/星云1.png" alt=""></div>
          <div class="swiper-slide" style="background-image:url(../assets/image/星云1.png)"><img src="../assets/image/星云2.png" alt=""></div>
        </div>
        <!-- Add Pagination -->
        <div class="swiper-pagination swiper-pagination-white" id="swiper-spit"></div>
        <!-- Add Arrows -->
        <div class="swiper-button-next swiper-button-white"></div>
        <div class="swiper-button-prev swiper-button-white"></div>
      </div>
    </div>

	  
    <div style="clear:both;"></div>
    <!-- Footer 版权信息 -->
    <NewFooterVue></NewFooterVue>
</div>
</template>
<script>
import axios from 'axios'
import qs from 'qs'

// 轮播图 【注意1】
import Swiper from 'swiper'; 
// import 'swiper/dist/css/swiper.min.css'
// import 'swiper/dist/js/swiper.min.js'


  export default {
    name: 'test',
    data() {
      return {
       
      };
    },
    mounted(){
     // 【注意2:】
      // 轮播图 · 初始化设定
       var swiper = new Swiper('.swiper-container', {
          spaceBetween: 30,
          effect: 'fade',
          autoplay: {
	          delay: 3000,
	          disableOnInteraction: false, // 取消鼠标操作后的轮播暂停【无操作轮播继续】【参考链接1】
	          stopOnLastSlide: false, // 在最后一页停止
	        },
          pagination: {
            el: '.swiper-pagination',
            clickable: true,
          },
          navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
          },

        });

    },
    methods: {  
    
    }
  }
</script>


<!--添加“范围”属性：“scoped”来限制CSS到这个组件 -->
<style scoped>
/* 轮播图 */
.swiper-container {width: 100%;height: 100%;}
.swiper-slide {background-position: center;background-size: cover;}
/* 焦点·参考swiper.min.css源文件修改 */


</style>