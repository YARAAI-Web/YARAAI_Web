rule auto_rule_20250726141750_9022 {
  strings:
    $o0 = "SetUserObjectInformationW" wide ascii nocase
    $o1 = "GetKeyNameTextW" wide ascii nocase
    $o2 = "pcbDataSize" wide ascii nocase
    $o3 = "MapVirtualKeyA" wide ascii nocase
    $o4 = "LookupIconIdFromDirectoryEx" wide ascii nocase
  condition:
    4 of ($o*)
}