rule auto_rule_20250726110107_8129 {
  strings:
    $o0 = "off_465F00" wide ascii nocase
    $o1 = "dword_47246C" wide ascii nocase
  condition:
    all of them
}