rule auto_rule_20250726135241_7412 {
  strings:
    $o0 = "SystemDrive" wide ascii nocase
    $o1 = "LdrEnumerateLoadedModules" wide ascii nocase
    $o2 = "NtAllocateVirtualMemory" wide ascii nocase
  condition:
    3 of ($o*)
}