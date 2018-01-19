/**
 * This file was automatically generated by json-schema-to-typescript.
 * DO NOT MODIFY IT BY HAND. Instead, modify the source JSONSchema file,
 * and run json-schema-to-typescript to regenerate this file.
 */

/**
 * Response shape for POST /api/adequacies/
 */
export type PostAdequaciesResponse = {
  id: number
  /**
   * Measure (in meters or minutes) to the closest provider
   */
  to_closest_provider: number
  closest_providers: number[]
}[]
