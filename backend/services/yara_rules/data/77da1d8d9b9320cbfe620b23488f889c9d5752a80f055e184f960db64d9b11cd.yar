rule auto_rule_20250727010945_9836 {
  strings:
    $o0 = "pUserData" wide ascii nocase
    $o1 = "GetStringTypeA" wide ascii nocase
    $o2 = "dword_464694" wide ascii nocase
  condition:
    3 of ($o*)
}