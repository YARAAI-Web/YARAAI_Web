rule auto_rule_20250727040034_3232 {
  strings:
    $o0 = "dword_4C1724" wide ascii nocase
    $o1 = "RegisterHotKey" wide ascii nocase
    $o2 = "SetExitCode" wide ascii nocase
    $o3 = "dword_4C15E0" wide ascii nocase
  condition:
    4 of ($o*)
}