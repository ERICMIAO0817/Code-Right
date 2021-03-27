<template>
  <div id="question">
    <!--顶部-->
    <div class="top">
      <h2 class="top_title">问卷调查</h2>
    </div>
    <!--大盒子-->
    <div class="content">
      <div class="answer_template">
        <div class="answer_top">MBTI职业性格测试</div>
        <div class="answer_top_line"></div>
        <div class="answer_box">
          <div class="answer_question">Q1:我倾向从何处得到动力和信心</div>
          <div class="answer_answer">
            <input type="radio" name="question_1" value="A" v-model="Q1" />
            A.别人
          </div>
          <div class="answer_answer">
            <input type="radio" name="question_1" value="B" v-model="Q1" />
            B.我自己的想法
          </div>
        </div>
        <div class="answer_box">
          <div class="answer_question">
            Q2:当我参加一个社交聚会时，我一般是这样的状态
          </div>
          <div class="answer_answer">
            <input type="radio" name="question_2" value="A" v-model="Q2" />
            A.夜色越深越有劲，一旦我开始投入，也许就是最晚离开的那一个
          </div>
          <div class="answer_answer">
            <input type="radio" name="question_2" value="B" v-model="Q2" />
            B.在夜晚开始的时候，我就疲倦了并且想回家
          </div>
        </div>
        <div class="answer_box">
          <div class="answer_question">Q3:下列哪一种听起来比较吸引人</div>
          <div class="answer_answer">
            <input type="radio" name="question_3" value="A" v-model="Q3" />
            A.与我的恋人到有很多人且社交活动频繁的地方
          </div>
          <div class="answer_answer">
            <input type="radio" name="question_3" value="B" v-model="Q3" />
            B.待在家中与我的恋人做一些特别的事情，例如说观赏一部有趣的录像带并享用我最爱的外带食物
          </div>
        </div>
        <div class="answer_box">
          <div class="answer_question">Q4:在约会中，我通常</div>
          <div class="answer_answer">
            <input type="radio" name="question_4" value="A" v-model="Q4" />
            A.整体来说蛮健谈的
          </div>
          <div class="answer_answer">
            <input type="radio" name="question_4" value="A" v-model="Q4" />
            B.较安静并保留，直到我觉得准备好了，才开始说话
          </div>
        </div>
        <div class="answer_box">
          <div class="answer_question">Q5:过去，我遇见我大部分恋人是</div>
          <div class="answer_answer">
            <input type="radio" name="question_5" value="A" v-model="Q5" />
            A.在公众场合，比如学习工作上、休闲活动中、或当朋友介绍我给他们的朋友时
          </div>
          <div class="answer_answer">
            <input type="radio" name="question_5" value="B" v-model="Q5" />
            B.透过私人的方式，例如婚恋网站、网络聊天、或是由亲密的朋友和家人介绍
          </div>
        </div>
        <div class="answer_box">
          <div class="answer_question">Q6:论真实的想法，我倾向拥有</div>
          <div class="answer_answer">
            <input type="radio" name="question_6" value="A" v-model="Q6" />
            A.很多认识的人和很亲密的朋友
          </div>
          <div class="answer_answer">
            <input type="radio" name="question_6" value="B" v-model="Q6" />
            B.一些很亲密的朋友和一些认识的人
          </div>
        </div>
        <div class="answer_box">
          <div class="answer_question">Q7:过去，我的恋人倾向对我说这些</div>
          <div class="answer_answer">
            <input type="radio" name="question_7" value="A" v-model="Q7" />
            A.你难道不可以安静一点吗
          </div>
          <div class="answer_answer">
            <input type="radio" name="question_7" value="B" v-model="Q7" />
            B.你能从自己的世界里面走出来一下吗
          </div>
        </div>
        <div class="answer_box">
          <div class="answer_question">
            Q8:我倾向透过以下方式形成脑海中的概念
          </div>
          <div class="answer_answer">
            <input type="radio" name="question_8" value="A" v-model="Q8" />
            A.我对有可能发生之事的想象和期望
          </div>
          <div class="answer_answer">
            <input type="radio" name="question_8" value="B" v-model="Q8" />
            B.我对目前状况实际认知
          </div>
        </div>
        <div class="answer_box">
          <div class="answer_question">
            Q9:在我做分析的时候，首先能意识到的是
          </div>
          <div class="answer_answer">
            <input type="radio" name="question_9" value="A" v-model="Q9" />
            A.我的直觉
          </div>
          <div class="answer_answer">
            <input type="radio" name="question_9" value="B" v-model="Q9" />
            B.我直接的观察和现成的经验
          </div>
        </div>
        <div class="answer_box">
          <div class="answer_question">
            Q10:在我自己的人际关系中，我一般是这样处理的
          </div>
          <div class="answer_answer">
            <input type="radio" name="question_10" value="A" v-model="Q10" />
            A.经常联络，因为永远有进步的空间
          </div>
          <div class="answer_answer">
            <input type="radio" name="question_10" value="B" v-model="Q10" />
            B.若它没有被破坏，别修补它
          </div>
        </div>
        <div class="answer_box">
          <div class="answer_question">
            Q11:当我在约会觉得放松时，我倾向谈论
          </div>
          <div class="answer_answer">
            <input type="radio" name="question_11" value="A" v-model="Q11" />
            A.未来，关于改进或发明事物，和生活的种种可能性。
          </div>
          <div class="answer_answer">
            <input type="radio" name="question_11" value="B" v-model="Q11" />
            B.实际的，具体的，关于「此时此地」的事物。
          </div>
        </div>
        <div class="answer_box">
          <div class="answer_question">Q12:我是这种人</div>
          <div class="answer_answer">
            <input type="radio" name="question_12" value="A" v-model="Q12" />
            A.先看整个大局面
          </div>
          <div class="answer_answer">
            <input type="radio" name="question_12" value="B" v-model="Q12" />
            B.先掌握细节
          </div>
        </div>
        <div class="answer_box">
          <div class="answer_question">Q13:在我内心深处，我认为</div>
          <div class="answer_answer">
            <input type="radio" name="question_13" value="A" v-model="Q13" />
            A.与其活在不完美的现实中，我选择活在我的精神世界里
          </div>
          <div class="answer_answer">
            <input type="radio" name="question_13" value="B" v-model="Q13" />
            B.与其活在虚无缥缈的精神世界，我选择活在现实中
          </div>
        </div>
        <div class="answer_box">
          <div class="answer_question">Q14:我通常：</div>
          <div class="answer_answer">
            <input type="radio" name="question_14" value="A" v-model="Q14" />
            A.偏向于去想象一大堆关于即将来临之约会的事情
          </div>
          <div class="answer_answer">
            <input type="radio" name="question_14" value="B" v-model="Q14" />
            B.偏向于拘紧地想象即将来临的约会，只期待让它自然地发生
          </div>
        </div>
        <div class="answer_box">
          <div class="answer_question">Q15:我倾向如此做决定</div>
          <div class="answer_answer">
            <input type="radio" name="question_15" value="A" v-model="Q15" />
            A.首先依我的心意，然后依我的逻辑
          </div>
          <div class="answer_answer">
            <input type="radio" name="question_15" value="B" v-model="Q15" />
            B.首先依我的逻辑，然后依我的心意
          </div>
        </div>
        <div class="answer_box">
          <div class="answer_question">Q16:我倾向比较能够察觉到</div>
          <div class="answer_answer">
            <input type="radio" name="question_16" value="A" v-model="Q16" />
            A.当人们需要情感上的支持时
          </div>
          <div class="answer_answer">
            <input type="radio" name="question_16" value="B" v-model="Q16" />
            B.当人们不合逻辑时
          </div>
        </div>
        <div class="answer_box">
          <div class="answer_question">Q17:当自己和某人分手时</div>
          <div class="answer_answer">
            <input type="radio" name="question_17" value="A" v-model="Q17" />
            A.我的情绪深陷其中，很难才能抽身而出
          </div>
          <div class="answer_answer">
            <input type="radio" name="question_17" value="B" v-model="Q17" />
            B.虽然我觉得受伤，但一旦下定决心，我会直截了当地将过去恋人的影子甩开
          </div>
        </div>
        <div class="answer_box">
          <div class="answer_question">Q18:当与一个人交往时，我倾向评量</div>
          <div class="answer_answer">
            <input type="radio" name="question_18" value="A" v-model="Q18" />
            A.情感上的兼容性：表达爱意和对另一半的需求很敏感
          </div>
          <div class="answer_answer">
            <input type="radio" name="question_18" value="B" v-model="Q18" />
            B.智能上的兼容性：沟通重要的想法：客观地讨论和辩论事情
          </div>
        </div>
        <div class="answer_box">
          <div class="answer_question">Q19:当我不同意我恋人的想法时：</div>
          <div class="answer_answer">
            <input type="radio" name="question_19" value="A" v-model="Q19" />
            A.我尽可能地避免伤害对方的感受；若是会对对方造成伤害的话，我就不会说
          </div>
          <div class="answer_answer">
            <input type="radio" name="question_19" value="B" v-model="Q19" />
            B.我通常很直接，毫无保留地把事实和我的逻辑告诉对方，因为对的就是对的
          </div>
        </div>
        <div class="answer_box">
          <div class="answer_question">Q20:认识我的人倾向形容我为：</div>
          <div class="answer_answer">
            <input type="radio" name="question_20" value="A" v-model="Q20" />
            A.热情和敏感
          </div>
          <div class="answer_answer">
            <input type="radio" name="question_20" value="B" v-model="Q20" />
            B.逻辑和明确
          </div>
        </div>
        <div class="answer_box">
          <div class="answer_question">Q21:我认为自己和很多人的相遇是：</div>
          <div class="answer_answer">
            <input type="radio" name="question_21" value="A" v-model="Q21" />
            A.随意的，友善的及重要的
          </div>
          <div class="answer_answer">
            <input type="radio" name="question_21" value="B" v-model="Q21" />
            B.经过思考的，或多或少有一定目的性
          </div>
        </div>
        <div class="answer_box">
          <div class="answer_question">
            Q22:若我有时间和金钱，我的朋友邀请我到国外度假，并且在一天前才通知，我会：
          </div>
          <div class="answer_answer">
            <input type="radio" name="question_22" value="A" v-model="Q22" />
            A.必须先检查我的时间表
          </div>
          <div class="answer_answer">
            <input type="radio" name="question_22" value="B" v-model="Q22" />
            B.立即收拾行装
          </div>
        </div>
        <div class="answer_box">
          <div class="answer_question">Q23:在第一次约会中：</div>
          <div class="answer_answer">
            <input type="radio" name="question_23" value="A" v-model="Q23" />
            A.若我所约的人来迟了，我心里会很不高兴
          </div>
          <div class="answer_answer">
            <input type="radio" name="question_23" value="B" v-model="Q23" />
            B.即使所约的人来迟了，我一点都不放在心里
          </div>
        </div>
        <div class="answer_box">
          <div class="answer_question">Q24:我偏好：</div>
          <div class="answer_answer">
            <input type="radio" name="question_24" value="A" v-model="Q24" />
            A.事先知道约会的行程：要去哪里、有谁参加、我会在哪里多久、该如何打扮
          </div>
          <div class="answer_answer">
            <input type="radio" name="question_24" value="B" v-model="Q24" />
            B.让约会自然地发生，不做先前太多的计划
          </div>
        </div>
        <div class="answer_box">
          <div class="answer_question">Q25:我期待的生活包含着：</div>
          <div class="answer_answer">
            <input type="radio" name="question_25" value="A" v-model="Q25" />
            A.科学合理的安排和有毅力的执行
          </div>
          <div class="answer_answer">
            <input type="radio" name="question_25" value="B" v-model="Q25" />
            B.没有什么压力，所有事情自然发生和时间弹性很大
          </div>
        </div>
        <div class="answer_box">
          <div class="answer_question">Q26:哪一项较为常见：</div>
          <div class="answer_answer">
            <input type="radio" name="question_26" value="A" v-model="Q26" />
            A.我先入会场而其它人随后来到
          </div>
          <div class="answer_answer">
            <input type="radio" name="question_26" value="B" v-model="Q26" />
            B.我先入会场而其它人随后来到
          </div>
        </div>
        <div class="answer_box">
          <div class="answer_question">Q27:我是这样喜欢……的人：</div>
          <div class="answer_answer">
            <input type="radio" name="question_27" value="A" v-model="Q27" />
            A.快刀斩乱麻，下定决心并且做出最后肯定的结论
          </div>
          <div class="answer_answer">
            <input type="radio" name="question_27" value="B" v-model="Q27" />
            B.放开我的选择并且持续收集信息，这样结果会更准确和深刻
          </div>
        </div>
        <div class="answer_box">
          <div class="answer_question">Q28:我是这类型的人：</div>
          <div class="answer_answer">
            <input type="radio" name="question_1" value="A" v-model="Q28" />
            A.喜欢在一个时间里专心于一件事情直到完成
          </div>
          <div class="answer_answer">
            <input type="radio" name="question_1" value="B" v-model="Q28" />
            B.喜欢同时进行好几件事情
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
@import url("../assets/question.css");
</style>

<script>
import axios from "axios";
import qs from "qs";
export default {
  name: "Question",
  data() {
    return {
      Q1: null,
      Q2: null,
      Q3: null,
      Q4: null,
      Q5: null,
      Q6: null,
      Q7: null,
      Q8: null,
      Q9: null,
      Q10: null,
      Q11: null,
      Q12: null,
      Q13: null,
      Q14: null,
      Q15: null,
      Q16: null,
      Q17: null,
      Q18: null,
      Q19: null,
      Q20: null,
      Q21: null,
      Q22: null,
      Q23: null,
      Q24: null,
      Q25: null,
      Q26: null,
      Q27: null,
      Q28: null,
      str: "",
    };
  },
  methods: {
    sendResult: function () {
      
      let data = {
        
      };
      axios: {
      }
    },
  },
  mounted() {
  },
};
</script>