rule auto_rule_20250726072825_7251 {
  strings:
    $o0 = "dword_41198C" wide ascii nocase
    $o1 = "dword_411ABC" wide ascii nocase
    $o2 = "dword_411E54" wide ascii nocase
    $o3 = "_seh_longjmp_unwind" wide ascii nocase
    $o4 = "CodePagea" wide ascii nocase
  condition:
    4 of ($o*)
}