rule auto_rule_20250726111421_3804 {
  strings:
    $o0 = "dword_449700" wide ascii nocase
    $o1 = "TrailDown2" wide ascii nocase
    $o2 = "dword_449938" wide ascii nocase
    $o3 = "UnwindUp1_0" wide ascii nocase
    $o4 = "_seh_longjmp_unwind" wide ascii nocase
  condition:
    4 of ($o*)
}