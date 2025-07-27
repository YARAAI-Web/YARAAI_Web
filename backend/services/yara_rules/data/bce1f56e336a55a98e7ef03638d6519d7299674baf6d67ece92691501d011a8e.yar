rule auto_rule_20250726132441_4919 {
  strings:
    $o0 = "dword_6403034C" wide ascii nocase
  condition:
    all of them
}