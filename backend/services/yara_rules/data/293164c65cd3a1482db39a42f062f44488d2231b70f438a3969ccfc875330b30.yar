rule auto_rule_20250726195055_4895 {
  strings:
    $o0 = "byte_6402A048" wide ascii nocase
    $o1 = "dword_64033340" wide ascii nocase
    $o2 = "dword_64033328" wide ascii nocase
  condition:
    3 of ($o*)
}