rule auto_rule_20250726124154_8625 {
  strings:
    $o0 = "dword_469B88" wide ascii nocase
    $o1 = "CPtoLCID" wide ascii nocase
  condition:
    all of them
}