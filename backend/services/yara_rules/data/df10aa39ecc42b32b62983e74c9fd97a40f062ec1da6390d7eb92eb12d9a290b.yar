rule auto_rule_20250726192141_5772 {
  strings:
    $o0 = "xmm7" wide ascii nocase
    $o1 = "xmmword_14053F1A0" wide ascii nocase
    $o2 = "x8D00700070008DLL" wide ascii nocase
    $o3 = "xmmword_14053F740" wide ascii nocase
  condition:
    4 of ($o*)
}