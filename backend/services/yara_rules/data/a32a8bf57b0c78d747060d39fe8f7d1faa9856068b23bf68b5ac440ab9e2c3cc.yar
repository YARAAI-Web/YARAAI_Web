rule auto_rule_20250727034101_9367 {
  strings:
    $o0 = "x1AA0u" wide ascii nocase
    $o1 = "dword_430363" wide ascii nocase
    $o2 = "x8364" wide ascii nocase
    $o3 = "prcClip" wide ascii nocase
  condition:
    4 of ($o*)
}