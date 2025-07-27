rule auto_rule_20250726072138_6906 {
  strings:
    $o0 = "SMapLS_IP_EBP_12" wide ascii nocase
    $o1 = "aXobglu32Dll_0" wide ascii nocase
  condition:
    all of them
}