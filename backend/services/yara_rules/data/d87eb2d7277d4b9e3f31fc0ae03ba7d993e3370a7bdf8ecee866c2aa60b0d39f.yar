rule auto_rule_20250727035940_1548 {
  strings:
    $o0 = "qword_18019D288" wide ascii nocase
    $o1 = "xmm6" wide ascii nocase
    $o2 = "x5F1A982025A185C6LL" wide ascii nocase
    $o3 = "qword_18019C398" wide ascii nocase
    $o4 = "xmmword_18019B008" wide ascii nocase
  condition:
    4 of ($o*)
}