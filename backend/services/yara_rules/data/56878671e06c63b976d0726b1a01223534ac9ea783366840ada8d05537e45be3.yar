rule auto_rule_20250726131351_8180 {
  strings:
    $o0 = "dword_1400DB97C" wide ascii nocase
    $o1 = "dword_1400DB5B4" wide ascii nocase
    $o2 = "dword_1400DB8A0" wide ascii nocase
    $o3 = "dword_1400DB554" wide ascii nocase
    $o4 = "dword_1400DB908" wide ascii nocase
  condition:
    4 of ($o*)
}