rule auto_rule_20250726184541_6315 {
  strings:
    $o0 = "hwndLock" wide ascii nocase
    $o1 = "pidl" wide ascii nocase
    $o2 = "pfImportCallback" wide ascii nocase
    $o3 = "dwDesiredAccess" wide ascii nocase
  condition:
    4 of ($o*)
}