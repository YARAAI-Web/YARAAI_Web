rule auto_rule_20250726102742_5447 {
  strings:
    $o0 = "_fpmath" wide ascii nocase
    $o1 = "dword_45712C" wide ascii nocase
    $o2 = "acmStreamClose" wide ascii nocase
  condition:
    3 of ($o*)
}