rule auto_rule_20250727024002_5727 {
  strings:
    $o0 = "byte_45DD74" wide ascii nocase
    $o1 = "_seh_longjmp_unwind" wide ascii nocase
    $o2 = "_heap_alloc" wide ascii nocase
    $o3 = "dword_460520" wide ascii nocase
    $o4 = "UnwindUp3_0" wide ascii nocase
  condition:
    4 of ($o*)
}