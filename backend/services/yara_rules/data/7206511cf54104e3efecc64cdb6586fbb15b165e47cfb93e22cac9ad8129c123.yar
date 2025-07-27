rule auto_rule_20250726062414_0117 {
  strings:
    $o0 = "dword_4012D4" wide ascii nocase
    $o1 = "aClsid13709620C" wide ascii nocase
  condition:
    all of them
}