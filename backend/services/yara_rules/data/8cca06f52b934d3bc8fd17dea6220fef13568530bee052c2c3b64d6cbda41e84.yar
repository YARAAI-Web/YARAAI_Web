rule auto_rule_20250726153035_7803 {
  strings:
    $o0 = "GetSidSubAuthority" wide ascii nocase
    $o1 = "dword_45D144" wide ascii nocase
    $o2 = "dword_428F00" wide ascii nocase
  condition:
    3 of ($o*)
}