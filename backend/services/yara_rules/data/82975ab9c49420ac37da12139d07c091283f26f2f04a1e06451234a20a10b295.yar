rule auto_rule_20250726231624_8362 {
  strings:
    $o0 = "wFatDate" wide ascii nocase
    $o1 = "lpSecurityAttributes" wide ascii nocase
    $o2 = "aStftware_0" wide ascii nocase
  condition:
    3 of ($o*)
}