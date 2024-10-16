(function(){"use strict";var t={5632:function(t,n,e){var o={};e.r(o);var r=e(5130),a=e(6768);const i={id:"app"};function s(t,n,e,o,r,s){const c=(0,a.g2)("router-view");return(0,a.uX)(),(0,a.CE)("div",i,[(0,a.bF)(c)])}var c={name:"App"},u=e(1241);const l=(0,u.A)(c,[["render",s]]);var p=l,d=e(1387);const m=(0,a.Lk)("h1",null,"Welcome to the Personal Finance Tracker",-1),f=(0,a.Lk)("button",null,"Add Transaction",-1);function v(t,n,e,o,r,i){const s=(0,a.g2)("router-link");return(0,a.uX)(),(0,a.CE)("div",null,[m,(0,a.bF)(s,{to:"/transactions"},{default:(0,a.k6)((()=>[f])),_:1})])}var h={name:"HomePage"};const b=(0,u.A)(h,[["render",v]]);var y=b,k=e(4232);const T=(0,a.Lk)("h1",null,"Add Transaction",-1),g=(0,a.Lk)("h2",null,"Transaction List",-1),L=(0,a.Lk)("h2",null,"Financial Summary",-1);function E(t,n,e,o,r,i){const s=(0,a.g2)("TransactionForm");return(0,a.uX)(),(0,a.CE)("div",null,[T,(0,a.bF)(s),(0,a.Lk)("div",null,[g,(0,a.Lk)("ul",null,[((0,a.uX)(!0),(0,a.CE)(a.FK,null,(0,a.pI)(i.transactions,(t=>((0,a.uX)(),(0,a.CE)("li",{key:t.description},(0,k.v_)(t.description)+": $"+(0,k.v_)(t.amount)+" ("+(0,k.v_)(t.type)+") ",1)))),128))]),L,(0,a.Lk)("p",null,"Total Income: $"+(0,k.v_)(i.totalIncome),1),(0,a.Lk)("p",null,"Total Expenses: $"+(0,k.v_)(i.totalExpenses),1),(0,a.Lk)("p",null,"Balance: $"+(0,k.v_)(i.balance),1)])])}const _=(0,a.Lk)("option",{value:"IN"},"Income",-1),O=(0,a.Lk)("option",{value:"EX"},"Expense",-1),A=[_,O],F=(0,a.Lk)("button",{type:"submit"},"Add Transaction",-1);function j(t,n,e,o,i,s){return(0,a.uX)(),(0,a.CE)("form",{onSubmit:n[3]||(n[3]=(0,r.D$)(((...t)=>s.submitForm&&s.submitForm(...t)),["prevent"]))},[(0,a.bo)((0,a.Lk)("input",{"onUpdate:modelValue":n[0]||(n[0]=t=>i.description=t),placeholder:"Description",required:""},null,512),[[r.Jo,i.description]]),(0,a.bo)((0,a.Lk)("input",{"onUpdate:modelValue":n[1]||(n[1]=t=>i.amount=t),type:"number",step:"0.01",placeholder:"Amount",required:""},null,512),[[r.Jo,i.amount]]),(0,a.bo)((0,a.Lk)("select",{"onUpdate:modelValue":n[2]||(n[2]=t=>i.transactionType=t),required:""},A,512),[[r.u1,i.transactionType]]),F],32)}var w=e(4373);w.A.create({baseURL:"http://localhost:8000/api",timeout:1e4,headers:{"Content-Type":"application/json"}});var $={data(){return{description:"",amount:"",transactionType:"IN"}},methods:{async submitForm(){const t={description:this.description,amount:this.amount,transaction_type:this.transactionType};await(0,o.createTransaction)(t),this.$emit("transactionCreated"),this.description="",this.amount="",this.transactionType="IN"}}};const x=(0,u.A)($,[["render",j]]);var C=x,I={components:{TransactionForm:C},computed:{transactions(){return this.$store.getters.allTransactions},totalIncome(){return this.$store.getters.totalIncome},totalExpenses(){return this.$store.getters.totalExpenses},balance(){return this.$store.getters.balance}}};const P=(0,u.A)(I,[["render",E]]);var S=P;const X=[{path:"/",name:"HomePage",component:y},{path:"/transactions",name:"TransactionsPage",component:S}],U=(0,d.aE)({history:(0,d.LA)(),routes:X});var q=U,M=e(782),N=(0,M.y$)({state:{transactions:[]},mutations:{setTransactions(t,n){t.transactions=n}},actions:{async fetchTransactions({commit:t}){try{const n=await w.A.get("/api/transactions");t("setTransactions",n.data)}catch(n){console.error("Error fetching transactions:",n)}}},modules:{}});const V=(0,r.Ef)(p);V.use(q),V.use(N),V.mount("#app")}},n={};function e(o){var r=n[o];if(void 0!==r)return r.exports;var a=n[o]={exports:{}};return t[o].call(a.exports,a,a.exports,e),a.exports}e.m=t,function(){var t=[];e.O=function(n,o,r,a){if(!o){var i=1/0;for(l=0;l<t.length;l++){o=t[l][0],r=t[l][1],a=t[l][2];for(var s=!0,c=0;c<o.length;c++)(!1&a||i>=a)&&Object.keys(e.O).every((function(t){return e.O[t](o[c])}))?o.splice(c--,1):(s=!1,a<i&&(i=a));if(s){t.splice(l--,1);var u=r();void 0!==u&&(n=u)}}return n}a=a||0;for(var l=t.length;l>0&&t[l-1][2]>a;l--)t[l]=t[l-1];t[l]=[o,r,a]}}(),function(){e.n=function(t){var n=t&&t.__esModule?function(){return t["default"]}:function(){return t};return e.d(n,{a:n}),n}}(),function(){e.d=function(t,n){for(var o in n)e.o(n,o)&&!e.o(t,o)&&Object.defineProperty(t,o,{enumerable:!0,get:n[o]})}}(),function(){e.g=function(){if("object"===typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(t){if("object"===typeof window)return window}}()}(),function(){e.o=function(t,n){return Object.prototype.hasOwnProperty.call(t,n)}}(),function(){e.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})}}(),function(){var t={524:0};e.O.j=function(n){return 0===t[n]};var n=function(n,o){var r,a,i=o[0],s=o[1],c=o[2],u=0;if(i.some((function(n){return 0!==t[n]}))){for(r in s)e.o(s,r)&&(e.m[r]=s[r]);if(c)var l=c(e)}for(n&&n(o);u<i.length;u++)a=i[u],e.o(t,a)&&t[a]&&t[a][0](),t[a]=0;return e.O(l)},o=self["webpackChunkmy_project"]=self["webpackChunkmy_project"]||[];o.forEach(n.bind(null,0)),o.push=n.bind(null,o.push.bind(o))}();var o=e.O(void 0,[504],(function(){return e(5632)}));o=e.O(o)})();
//# sourceMappingURL=app.a2cf6fab.js.map