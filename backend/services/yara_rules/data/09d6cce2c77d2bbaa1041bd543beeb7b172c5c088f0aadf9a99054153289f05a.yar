rule auto_rule_20250726113352_7837 {
  strings:
    $o0 = "tail_loop_start" wide ascii nocase
    $o1 = "GdipCreateFontFamilyFromName" wide ascii nocase
    $o2 = "dword_454F0C" wide ascii nocase
  condition:
    3 of ($o*)
}