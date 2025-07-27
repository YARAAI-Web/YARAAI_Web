rule auto_rule_20250726070808_4173 {
  strings:
    $o0 = "qword_140024390" wide ascii nocase
    $o1 = "x10uLL" wide ascii nocase
    $o2 = "qword_140031068" wide ascii nocase
    $o3 = "x2818u" wide ascii nocase
  condition:
    4 of ($o*)
}