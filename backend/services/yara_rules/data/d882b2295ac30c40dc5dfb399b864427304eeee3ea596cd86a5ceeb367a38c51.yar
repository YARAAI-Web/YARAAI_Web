rule auto_rule_20250726233153_8399 {
  strings:
    $o0 = "off_41B1A8" wide ascii nocase
    $o1 = "dword_41B224" wide ascii nocase
    $o2 = "x3333u" wide ascii nocase
    $o3 = "wvsprintfA" wide ascii nocase
    $o4 = "FileTimeToDosDateTime" wide ascii nocase
  condition:
    4 of ($o*)
}