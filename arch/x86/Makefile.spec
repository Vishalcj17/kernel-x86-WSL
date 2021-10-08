# for CONFIG_OPTIMIZE_SPECIFICALLY
# gcc -march=native -E -v - </dev/null 2>&1 | grep cc1

cflags-$(CONFIG_OPTIMIZE_FOR_11300H)   += -march=tigerlake -mmmx -mno-3dnow -msse -msse2 -msse3 -mssse3 -mno-sse4a -mcx16 -msahf -mmovbe -maes -msha -mpclmul -mpopcnt -mabm -mno-lwp -mfma -mno-fma4 -mno-xop -mbmi -mno-sgx -mbmi2 -mno-pconfig -mno-wbnoinvd -mno-tbm -mavx -mavx2 -msse4.2 -msse4.1 -mlzcnt -mno-rtm -mno-hle -mrdrnd -mf16c -mfsgsbase -mrdseed -mprfchw -madx -mfxsr -mxsave -mxsaveopt -mavx512f -mno-avx512er -mavx512cd -mno-avx512pf -mno-prefetchwt1 -mclflushopt -mxsavec -mxsaves -mavx512dq -mavx512bw -mavx512vl -mavx512ifma -mavx512vbmi -mno-avx5124fmaps -mno-avx5124vnniw -mclwb -mno-mwaitx -mno-clzero -mno-pku -mrdpid -mgfni -mshstk -mavx512vbmi2 -mavx512vnni -mvaes -mvpclmulqdq -mavx512bitalg -mavx512vpopcntdq -mmovdiri -mmovdir64b -mno-waitpkg -mno-cldemote -mno-ptwrite --param l1-cache-size=48 --param l1-cache-line-size=64 --param l2-cache-size=8192 -mtune=tigerlake -fasynchronous-unwind-tables -fstack-protector-strong -Wformat -Wformat-security -fstack-clash-protection

# from arch/x86/Makefile: Prevent GCC from generating any FP code by mistake.
cflags-$(CONFIG_OPTIMIZE_SPECIFICALLY) += -mno-sse -mno-mmx -mno-sse2 -mno-3dnow
cflags-$(CONFIG_OPTIMIZE_SPECIFICALLY) += $(call cc-option,-mno-avx,)
