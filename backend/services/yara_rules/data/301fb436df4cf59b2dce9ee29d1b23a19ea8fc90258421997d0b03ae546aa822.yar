rule auto_rule_20250726112915_5658 {
  strings:
    $o0 = "memcpy_0" wide ascii nocase
    $o1 = "off_463AE8" wide ascii nocase
    $o2 = "dword_4643D8" wide ascii nocase
    $o3 = "_seh_longjmp_unwind" wide ascii nocase
    $o4 = "nModule" wide ascii nocase
  condition:
    4 of ($o*)
}