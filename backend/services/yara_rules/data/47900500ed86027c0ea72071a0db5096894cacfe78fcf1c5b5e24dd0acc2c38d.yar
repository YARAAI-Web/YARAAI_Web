rule auto_rule_20250726201713_8630 {
  strings:
    $o0 = "GetWindowModuleFileNameA" wide ascii nocase
    $o1 = "RemovePropW" wide ascii nocase
    $o2 = "fSearchOp" wide ascii nocase
    $o3 = "SetVolumeMountPointA" wide ascii nocase
  condition:
    4 of ($o*)
}