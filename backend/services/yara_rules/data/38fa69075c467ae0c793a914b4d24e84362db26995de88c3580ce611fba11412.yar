rule auto_rule_20250727032644_9528 {
  strings:
    $o0 = "dword_7E35C" wide ascii nocase
    $o1 = "dword_1E92C" wide ascii nocase
    $o2 = "dword_7F714" wide ascii nocase
    $o3 = "PoolWithTag" wide ascii nocase
  condition:
    4 of ($o*)
}