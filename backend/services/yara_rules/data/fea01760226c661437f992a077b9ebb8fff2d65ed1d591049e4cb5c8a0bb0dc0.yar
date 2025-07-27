rule auto_rule_20250726153822_0293 {
  strings:
    $o0 = "qword_140118D38" wide ascii nocase
    $o1 = "qword_140115318" wide ascii nocase
    $o2 = "byte_140116800" wide ascii nocase
    $o3 = "below" wide ascii nocase
  condition:
    4 of ($o*)
}