rule auto_rule_20250726072511_3185 {
  strings:
    $o0 = "dwDesiredAccess" wide ascii nocase
    $o1 = "dword_42EECC" wide ascii nocase
    $o2 = "a24gop333eya" wide ascii nocase
  condition:
    3 of ($o*)
}