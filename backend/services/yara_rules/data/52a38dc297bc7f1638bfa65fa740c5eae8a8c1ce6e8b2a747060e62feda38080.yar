rule auto_rule_20250727022430_9835 {
  strings:
    $o0 = "start_byte_3" wide ascii nocase
    $o1 = "dword_412238" wide ascii nocase
    $o2 = "TrailDown1" wide ascii nocase
  condition:
    3 of ($o*)
}