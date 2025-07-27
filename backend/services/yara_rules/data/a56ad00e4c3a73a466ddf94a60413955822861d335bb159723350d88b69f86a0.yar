rule auto_rule_20250726170621_8570 {
  strings:
    $o0 = "GetClipboardViewer" wide ascii nocase
    $o1 = "lpInfo" wide ascii nocase
    $o2 = "fInherit" wide ascii nocase
    $o3 = "lpFilePart" wide ascii nocase
    $o4 = "dwOpenMode" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726170625_1560 {
  strings:
    $o0 = "iIconIndex" wide ascii nocase
    $o1 = "lpszVolumeMountPoint" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726170628_8856 {
  condition:
    auto_rule_20250726170621_8570 or auto_rule_20250726170625_1560
}