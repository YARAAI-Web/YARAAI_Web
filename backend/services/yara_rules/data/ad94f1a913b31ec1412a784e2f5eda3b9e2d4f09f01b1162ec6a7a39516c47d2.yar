rule auto_rule_20250726201336_4698 {
  strings:
    $o0 = "RegisterHotKey" wide ascii nocase
    $o1 = "dword_4C131C" wide ascii nocase
    $o2 = "TaskbarCreated" wide ascii nocase
    $o3 = "isdigit" wide ascii nocase
  condition:
    4 of ($o*)
}