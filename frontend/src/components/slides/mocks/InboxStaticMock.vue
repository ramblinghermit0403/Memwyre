<template>
  <div class="w-full h-full font-sans">
    <!-- Literal UI provided by USER -->
    <div class="w-full flex flex-col bg-[#111111] rounded-xl shadow-[0_4rem_10rem_rgba(0,0,0,0.9)] border border-white/10 overflow-hidden">
      
      <div class="p-5 border-b border-white/5 flex justify-between items-center bg-[#0a0a0a]">
        <h2 class="text-base font-bold text-white uppercase tracking-widest italic opacity-80">Incoming Items</h2>
      </div>

      <div class="flex-1 overflow-y-auto p-4 space-y-4 custom-scrollbar bg-transparent pointer-events-none">
        
        <!-- Item 1: Claude -->
        <div class="p-5 rounded-lg border bg-[#1a1a1a] border-white/5">
          <h3 class="font-bold text-gray-900 dark:text-gray-100 mb-1 line-clamp-2">Test Memory from Claude</h3>
          <div class="flex justify-between items-end mt-3">
            <div class="flex flex-col gap-2">
              <div class="flex items-center gap-2">
                <div class="w-5 h-5 flex items-center justify-center shrink-0 text-gray-400 dark:text-gray-500 rounded overflow-hidden">
                  <img src="data:image/svg+xml,%3csvg%20height='1em'%20style='flex:none;line-height:1'%20viewBox='0%200%2024%2024'%20width='1em'%20xmlns='http://www.w3.org/2000/svg'%3e%3ctitle%3eClaude%3c/title%3e%3cpath%20d='M4.709%2015.955l4.72-2.647.08-.23-.08-.128H9.2l-.79-.048-2.698-.073-2.339-.097-2.266-.122-.571-.121L0%2011.784l.055-.352.48-.321.686.06%201.52.103%202.278.158%201.652.097%202.449.255h.389l.055-.157-.134-.098-.103-.097-2.358-1.596-2.552-1.688-1.336-.972-.724-.491-.364-.462-.158-1.008.656-.722.881.06.225.061.893.686%201.908%201.476%202.491%201.833.365.304.145-.103.019-.073-.164-.274-1.355-2.446-1.446-2.49-.644-1.032-.17-.619a2.97%202.97%200%2001-.104-.729L6.283.134%206.696%200l.996.134.42.364.62%201.414%201.002%202.229%201.555%203.03.456.898.243.832.091.255h.158V9.01l.128-1.706.237-2.095.23-2.695.08-.76.376-.91.747-.492.584.28.48.685-.067.444-.286%201.851-.559%202.903-.364%201.942h.212l.243-.242.985-1.306%201.652-2.064.73-.82.85-.904.547-.431h1.033l.76%201.129-.34%201.166-1.064%201.347-.881%201.142-1.264%201.7-.79%201.36.073.11.188-.02%202.856-.606%201.543-.28%201.841-.315.833.388.091.395-.328.807-1.969.486-2.309.462-3.439.813-.042.03.049.061%201.549.146.662.036h1.622l3.02.225.79.522.474.638-.079.485-1.215.62-1.64-.389-3.829-.91-1.312-.329h-.182v.11l1.093%201.068%202.006%201.81%202.509%202.33.127.578-.322.455-.34-.049-2.205-1.657-.851-.747-1.926-1.62h-.128v.17l.444.649%202.345%203.521.122%201.08-.17.353-.608.213-.668-.122-1.374-1.925-1.415-2.167-1.143-1.943-.14.08-.674%207.254-.316.37-.729.28-.607-.461-.322-.747.322-1.476.389-1.924.315-1.53.286-1.9.17-.632-.012-.042-.14.018-1.434%201.967-2.18%202.945-1.726%201.845-.414.164-.717-.37.067-.662.401-.589%202.388-3.036%201.44-1.882.93-1.086-.006-.158h-.055L4.132%2018.56l-1.13.146-.487-.456.061-.746.231-.243%201.908-1.312-.006.006z'%20fill='%23D97757'%20fill-rule='nonzero'%3e%3c/path%3e%3c/svg%3e" alt="Source" class="w-full h-full object-cover rounded-sm">
                </div>
                <span class="text-xs text-gray-600 dark:text-gray-400 truncate max-w-[140px] font-mono">claude</span>
              </div>
              <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-bold w-fit bg-emerald-950/30 text-emerald-300 border border-emerald-900/40 uppercase tracking-widest">Approved</span>
            </div>
            <span class="text-[10px] font-bold text-gray-500">3d ago</span>
          </div>
        </div>

        <!-- Item 2: Antigravity -->
        <div class="p-5 rounded-lg border bg-[#1a1a1a] border-[#D97757]">
          <h3 class="font-bold text-gray-900 dark:text-gray-100 mb-1 line-clamp-2">Test Memory for Memwyre Integration</h3>
          <div class="flex justify-between items-end mt-3">
            <div class="flex flex-col gap-2">
              <div class="flex items-center gap-2">
                <div class="w-5 h-5 flex items-center justify-center shrink-0 text-gray-400 dark:text-gray-500 rounded overflow-hidden">
                  <img src="@/assets/Google-Antigravity-Icon-Full-Color.png" alt="Source" class="w-full h-full object-cover rounded-sm">
                </div>
                <span class="text-xs text-gray-600 dark:text-gray-400 truncate max-w-[140px] font-mono">antigravity</span>
              </div>
              <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-bold w-fit bg-emerald-950/30 text-emerald-300 border border-emerald-900/40 uppercase tracking-widest">Approved</span>
            </div>
            <span class="text-[10px] font-bold text-gray-500">3d ago</span>
          </div>
        </div>

        <!-- Item 3: ChatGPT -->
        <div class="p-5 rounded-lg border bg-[#1a1a1a] border-white/5">
          <h3 class="font-bold text-gray-900 dark:text-gray-100 mb-1 line-clamp-2">Enhancing AI Idea Retention</h3>
          <div class="flex justify-between items-end mt-3">
            <div class="flex flex-col gap-2">
              <div class="flex items-center gap-2">
                <div class="w-5 h-5 flex items-center justify-center shrink-0 text-gray-400 dark:text-gray-500 rounded overflow-hidden">
                  <img src="data:image/svg+xml,%3csvg%20fill-rule='evenodd'%20height='1em'%20style='flex:none;line-height:1'%20viewBox='0%200%2024%2024'%20width='1em'%20xmlns='http://www.w3.org/2000/svg'%3e%3cstyle%3epath%20{%20fill:%20%23111111;%20}%3c/style%3e%3ctitle%3eOpenAI%3c/title%3e%3cpath%20d='M9.205%208.658v-2.26c0-.19.072-.333.238-.428l4.543-2.616c.619-.357%201.356-.523%202.117-.523%202.854%200%204.662%202.212%204.662%204.566%200%20.167%200%20.357-.024.547l-4.71-2.759a.797.797%200%2000-.856%200l-5.97%203.473zm10.609%208.8V12.06c0-.333-.143-.57-.429-.737l-5.97-3.473%201.95-1.118a.433.433%200%2001.476%200l4.543%202.617c1.309.76%202.189%202.378%202.189%203.948%200%201.808-1.07%203.473-2.76%204.163zM7.802%2012.703l-1.95-1.142c-.167-.095-.239-.238-.239-.428V5.899c0-2.545%201.95-4.472%204.591-4.472%201%200%201.927.333%202.712.928L8.23%205.067c-.285.166-.428.404-.428.737v6.898zM12%2015.128l-2.795-1.57v-3.33L12%208.658l2.795%201.57v3.33L12%2015.128zm1.796%207.23c-1%200-1.927-.332-2.712-.927l4.686-2.712c.285-.166.428-.404.428-.737v-6.898l1.974%201.142c.167.095.238.238.238.428v5.233c0%202.545-1.974%204.472-4.614%204.472zm-5.637-5.303l-4.544-2.617c-1.308-.761-2.188-2.378-2.188-3.948A4.482%204.482%200%20014.21%206.327v5.423c0%20.333.143.571.428.738l5.947%203.449-1.95%201.118a.432.432%200%2001-.476%200zm-.262%203.9c-2.688%200-4.662-2.021-4.662-4.519%200-.19.024-.38.047-.57l4.686%202.71c.286.167.571.167.856%200l5.97-3.448v2.26c0%20.19-.07.333-.237.428l-4.543%202.616c-.619.357-1.356.523-2.117.523zm5.899%202.83a5.947%205.947%200%20005.827-4.756C22.287%2018.339%2024%2015.84%2024%2013.296c0-1.665-.713-3.282-1.998-4.448.119-.5.19-.999.19-1.498%200-3.401-2.759-5.947-5.946-5.947-.642%200-1.26-.095-1.88-.31A5.962%205.962%200%200010.205%200a5.947%205.947%200%2000-5.827%204.757C1.713%205.447%200%207.945%200%2010.49c0%201.666.713%203.283%201.998%204.448-.119.5-.19%201-.19%201.499%200%203.401%202.759%205.946%205.946%205.946.642%200%201.26-.095%201.88-.309a5.96%205.96%200%20004.162%201.713z'%3e%3c/path%3e%3c/svg%3e" alt="Source" class="w-full h-full object-cover rounded-sm dark:invert opacity-80">
                </div>
                <span class="text-xs text-gray-600 dark:text-gray-400 truncate max-w-[140px] font-mono">chatgpt</span>
              </div>
              <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-bold w-fit bg-emerald-950/30 text-emerald-300 border border-emerald-900/40 uppercase tracking-widest">Approved</span>
            </div>
            <span class="text-[10px] font-bold text-gray-500">6d ago</span>
          </div>
        </div>

        <!-- Item 4: Dodo Payments (Approved) -->
        <div class="p-5 rounded-lg border bg-[#1a1a1a] border-white/5">
          <h3 class="font-bold text-gray-900 dark:text-gray-100 mb-1 line-clamp-2">Dodo Payments Configuration</h3>
          <div class="flex justify-between items-end mt-3">
            <div class="flex flex-col gap-2">
              <div class="flex items-center gap-2">
                <div class="w-5 h-5 flex items-center justify-center shrink-0 text-gray-400 dark:text-gray-500 rounded overflow-hidden">
                  <div class="w-full h-full">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" class="w-full h-full">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path>
                    </svg>
                  </div>
                </div>
                <span class="text-xs text-gray-600 dark:text-gray-400 truncate max-w-[140px] font-mono">web observer</span>
              </div>
              <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-bold w-fit bg-emerald-950/30 text-emerald-300 border border-emerald-900/40 uppercase tracking-widest">Approved</span>
            </div>
            <span class="text-[10px] font-bold text-gray-500">15d ago</span>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script setup>
// Final stylized literal component from USER source
</script>

<style scoped>
.custom-scrollbar::-webkit-scrollbar {
  width: 4px;
}
.custom-scrollbar::-webkit-scrollbar-track {
  background: transparent;
}
.custom-scrollbar::-webkit-scrollbar-thumb {
  background: rgba(255, 255, 255, 0.1);
  border-radius: 10px;
}
</style>
